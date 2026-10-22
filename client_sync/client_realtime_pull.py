import os
import sys
import time
import subprocess
from datetime import datetime

# Cấu hình
CHECK_INTERVAL_SECONDS = 5  # Quét kiểm tra bản mới mỗi 5 giây
BRANCH = "main"             # Nhánh nhận cập nhật (main hoặc dev)

# Đảm bảo hiển thị Tiếng Việt trên Console Windows
if sys.stdout is not None:
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
# Nếu đặt file trong thư mục client_sync con, thư mục repo là cha của nó
if os.path.exists(os.path.join(CURRENT_DIR, ".git")):
    REPO_DIR = CURRENT_DIR
else:
    REPO_DIR = os.path.abspath(os.path.join(CURRENT_DIR, ".."))

def log(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {msg}", flush=True)

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
    log("  ĐỒNG BỘ MÁY CON (CLIENT READ-ONLY AUTO-SYNC)")
    log(f"  - Thư mục dữ liệu: {REPO_DIR}")
    log(f"  - Nhánh theo dõi: origin/{BRANCH}")
    log(f"  - Chu kỳ kiểm tra: mỗi {CHECK_INTERVAL_SECONDS} giây")
    log("=" * 65)
    log("Đang theo dõi các cập nhật mới nhất từ GitHub...")

    while True:
        try:
            # 1. Lấy thông tin mới nhất từ remote
            code, _, _ = run_cmd("git fetch origin")
            if code == 0:
                # So sánh mã commit HEAD hiện tại với remote
                _, local_hash, _ = run_cmd("git rev-parse HEAD")
                _, remote_hash, _ = run_cmd(f"git rev-parse origin/{BRANCH}")

                if local_hash and remote_hash and local_hash != remote_hash:
                    log(f"⚡ Phát hiện bản cập nhật mới trên GitHub ({remote_hash[:7]})!")
                    log("   Đang tự động kéo dữ liệu về máy...")

                    # Sử dụng reset --hard để luôn luôn khớp 100% với máy chủ gốc
                    # (kể cả khi người dùng máy con có lỡ chỉnh sửa hay xóa file)
                    run_cmd(f"git reset --hard origin/{BRANCH}")
                    run_cmd("git clean -fd")

                    log(f"✅ Đồng bộ hoàn tất! Dữ liệu trên máy đã cập nhật 100% giống máy chủ.\n")
                    log("Tiếp tục lắng nghe thay đổi...")

            time.sleep(CHECK_INTERVAL_SECONDS)

        except KeyboardInterrupt:
            log("\nĐã dừng đồng bộ máy con theo yêu cầu.")
            break
        except Exception as e:
            log(f"Lỗi: {e}")
            time.sleep(CHECK_INTERVAL_SECONDS)

if __name__ == "__main__":
    main()
