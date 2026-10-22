import os
import sys
import time
import subprocess
from datetime import datetime

CHECK_INTERVAL_SECONDS = 5  # Quét kiểm tra bản mới mỗi 5 giây
BRANCH = "main"             # Nhánh nhận cập nhật (main)

if sys.stdout is not None:
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
if sys.stderr is not None:
    try:
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
if os.path.exists(os.path.join(CURRENT_DIR, ".git")):
    REPO_DIR = CURRENT_DIR
else:
    REPO_DIR = os.path.abspath(os.path.join(CURRENT_DIR, ".."))

LOG_FILE = os.path.join(CURRENT_DIR, "client_sync.log")

def log(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_msg = f"[{timestamp}] {msg}"
    if sys.stdout is not None:
        try:
            print(full_msg, flush=True)
        except Exception:
            pass
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(full_msg + "\n")
    except Exception:
        pass

def run_cmd(cmd):
    try:
        res = subprocess.run(
            cmd, cwd=REPO_DIR, shell=True, capture_output=True, text=True, encoding='utf-8', errors='replace'
        )
        return res.returncode, res.stdout.strip(), res.stderr.strip()
    except Exception as e:
        return -1, "", str(e)

def main():
    log("=" * 65)
    log("  ĐỒNG BỘ MÁY CON (CLIENT READ-ONLY AUTO-SYNC) ĐÃ KHỞI ĐỘNG")
    log(f"  - Thư mục dữ liệu: {REPO_DIR}")
    log(f"  - Nhánh theo dõi: origin/{BRANCH}")
    log(f"  - Chu kỳ kiểm tra: mỗi {CHECK_INTERVAL_SECONDS} giây")
    log("=" * 65)

    consecutive_network_errors = 0

    while True:
        try:
            code, _, err = run_cmd("git fetch origin")
            if code == 0:
                consecutive_network_errors = 0
                _, local_hash, _ = run_cmd("git rev-parse HEAD")
                _, remote_hash, _ = run_cmd(f"git rev-parse origin/{BRANCH}")

                if local_hash and remote_hash and local_hash != remote_hash:
                    log(f"⚡ Phát hiện bản cập nhật mới trên GitHub ({remote_hash[:7]})!")
                    log("   Đang kéo dữ liệu về máy...")

                    # Đảm bảo 100% khớp máy chủ, loại bỏ mọi thay đổi cục bộ ở máy con
                    run_cmd(f"git reset --hard origin/{BRANCH}")
                    # Giữ lại thư mục client_sync và file log
                    run_cmd("git clean -fd -e client_sync/")

                    log("✅ Đồng bộ hoàn tất! Dữ liệu trên máy đã cập nhật 100% giống máy chủ.\n")
            else:
                consecutive_network_errors += 1
                # Nếu vừa khởi động máy chưa có mạng, ghi log nhẹ nhàng không crash
                if consecutive_network_errors == 1:
                    log("Đang chờ kết nối Internet để đồng bộ...")

            time.sleep(CHECK_INTERVAL_SECONDS)

        except KeyboardInterrupt:
            log("Đã dừng tiến trình theo yêu cầu.")
            break
        except Exception as e:
            log(f"Lỗi: {e}")
            time.sleep(CHECK_INTERVAL_SECONDS)

if __name__ == "__main__":
    main()
