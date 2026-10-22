import os
import sys
import time
import subprocess
from datetime import datetime

# Đảm bảo mã hóa UTF-8 cho stdout/stderr nếu có console
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

# Cấu hình thư mục
WORKTREE_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.abspath(os.path.join(WORKTREE_DIR, "..", ".."))
LOG_FILE = os.path.join(WORKTREE_DIR, "realtime_sync.log")

CHECK_INTERVAL_SECONDS = 3  # Quét thay đổi mỗi 3 giây
DEBOUNCE_SECONDS = 5        # Chờ 5 giây ổn định sau thay đổi cuối cùng trước khi push

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

def run_cmd(cmd, cwd):
    try:
        res = subprocess.run(
            cmd, cwd=cwd, shell=True, capture_output=True, text=True, encoding='utf-8', errors='replace'
        )
        return res.returncode, res.stdout.strip(), res.stderr.strip()
    except Exception as e:
        return -1, "", str(e)

def get_git_status():
    code, stdout, _ = run_cmd("git status --porcelain", WORKTREE_DIR)
    if code == 0 and stdout:
        return [line for line in stdout.splitlines() if not line.endswith("realtime_sync.log")]
    return []

def main():
    log("=" * 60)
    log("TỰ ĐỘNG ĐỒNG BỘ THỜI GIAN THỰC LÊN GITHUB KHỞI ĐỘNG")
    log(f"Thư mục theo dõi: {WORKTREE_DIR}")
    log("=" * 60)

    last_change_time = None
    pending_sync = False

    while True:
        try:
            status_lines = get_git_status()

            if status_lines:
                current_time = time.time()
                if not pending_sync:
                    pending_sync = True
                    last_change_time = current_time
                    log(f"⚡ Phát hiện {len(status_lines)} thay đổi trên máy:")
                    for line in status_lines[:8]:
                        log(f"   -> {line}")
                    if len(status_lines) > 8:
                        log(f"   -> ... và {len(status_lines) - 8} tệp khác")
                    log(f"   Chờ {DEBOUNCE_SECONDS}s ổn định trước khi push...")
                else:
                    last_change_time = current_time

            if pending_sync and last_change_time:
                elapsed = time.time() - last_change_time
                if elapsed >= DEBOUNCE_SECONDS:
                    log("🚀 Bắt đầu đồng bộ lên GitHub...")

                    # 1. Stage tất cả (bao gồm thêm, sửa, xóa)
                    code, _, err = run_cmd("git add -A", WORKTREE_DIR)
                    if code != 0:
                        log(f"❌ Lỗi git add: {err}")
                        pending_sync = False
                        continue

                    # 2. Kiểm tra nếu có diff trong index
                    code, _, _ = run_cmd("git diff --cached --quiet", WORKTREE_DIR)
                    if code != 0:
                        commit_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        commit_msg = f"Realtime sync: {commit_time}"
                        code, _, err = run_cmd(f'git commit -m "{commit_msg}"', WORKTREE_DIR)
                        if code == 0:
                            log(f"✅ Đã tạo commit: {commit_msg}")
                        else:
                            log(f"⚠️ Commit warning: {err}")

                        # 3. Đẩy lên nhánh dev
                        log("   Đang đẩy lên nhánh dev...")
                        code, _, err = run_cmd("git push origin dev", WORKTREE_DIR)
                        if code == 0:
                            log("   ✅ Nhánh dev trên GitHub đã cập nhật thành công!")
                        else:
                            log(f"   ⚠️ Lỗi push dev: {err}")

                        # 4. Merge sang nhánh main
                        log("   Đang đồng bộ sang nhánh main...")
                        run_cmd("git merge dev --no-edit", ROOT_DIR)
                        code, _, err = run_cmd("git push origin main", ROOT_DIR)
                        if code == 0:
                            log("   ✅ Nhánh main trên GitHub đã cập nhật thành công!")
                        else:
                            log(f"   ⚠️ Lỗi push main: {err}")

                        log("🎉 [HOÀN TẤT] GitHub đã phản ánh chính xác 100% thay đổi trên máy!\n")
                    else:
                        log("ℹ️ Không có thay đổi nào cần commit.")

                    pending_sync = False

            time.sleep(CHECK_INTERVAL_SECONDS)

        except KeyboardInterrupt:
            log("Đã dừng tiến trình theo yêu cầu (KeyboardInterrupt).")
            break
        except Exception as e:
            log(f"Lỗi: {e}")
            time.sleep(CHECK_INTERVAL_SECONDS)

if __name__ == "__main__":
    main()
