import os
import sys
import time
import subprocess
from datetime import datetime

# Cấu hình thư mục
WORKTREE_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.abspath(os.path.join(WORKTREE_DIR, "..", ".."))

CHECK_INTERVAL_SECONDS = 3  # Quét thay đổi mỗi 3 giây
DEBOUNCE_SECONDS = 5        # Chờ 5 giây ổn định sau thay đổi cuối cùng trước khi push

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
        return stdout.splitlines()
    return []

def main():
    print("=" * 65)
    print("  TỰ ĐỘNG ĐỒNG BỘ THỜI GIAN THỰC LÊN GITHUB (REALTIME SYNC)")
    print(f"  - Thư mục Worktree: {WORKTREE_DIR}")
    print(f"  - Chu kỳ kiểm tra: mỗi {CHECK_INTERVAL_SECONDS} giây")
    print("=" * 65)
    print("Đang lắng nghe các thay đổi tập tin (Thêm / Sửa / Xóa)...")
    print("Nhấn Ctrl + C để dừng bất kỳ lúc nào.\n")

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
                    now_str = datetime.now().strftime("%H:%M:%S")
                    print(f"[{now_str}] ⚡ Phát hiện {len(status_lines)} thay đổi trên máy:")
                    for line in status_lines[:8]:
                        print(f"   -> {line}")
                    if len(status_lines) > 8:
                        print(f"   -> ... và {len(status_lines) - 8} tệp khác")
                    print(f"   Chờ {DEBOUNCE_SECONDS}s gom nhóm thao tác trước khi đẩy lên GitHub...")
                else:
                    # Nếu vẫn còn file đang tiếp tục được sửa/thêm/xóa, dời thời điểm push
                    last_change_time = current_time

            # Nếu có thay đổi và đã qua thời gian debounce
            if pending_sync and last_change_time:
                elapsed = time.time() - last_change_time
                if elapsed >= DEBOUNCE_SECONDS:
                    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"\n[{now_str}] 🚀 Đang tiến hành đồng bộ lên GitHub...")

                    # 1. Stage tất cả (kể cả xóa file)
                    code, _, err = run_cmd("git add -A", WORKTREE_DIR)
                    if code != 0:
                        print(f"❌ Lỗi khi git add: {err}")
                        pending_sync = False
                        continue

                    # 2. Kiểm tra nếu có diff trong index
                    code, _, _ = run_cmd("git diff --cached --quiet", WORKTREE_DIR)
                    if code != 0:
                        commit_msg = f"Realtime sync: {now_str}"
                        code, _, err = run_cmd(f'git commit -m "{commit_msg}"', WORKTREE_DIR)
                        if code == 0:
                            print(f"✅ Đã tạo commit: {commit_msg}")
                        else:
                            print(f"⚠️ Commit warning: {err}")

                        # 3. Đẩy lên nhánh dev
                        print("   Đang đẩy lên nhánh dev...")
                        code, _, err = run_cmd("git push origin dev", WORKTREE_DIR)
                        if code == 0:
                            print("   ✅ Nhánh dev trên GitHub đã cập nhật!")
                        else:
                            print(f"   ⚠️ Lỗi push dev: {err}")

                        # 4. Merge sang main và đẩy lên main
                        print("   Đang đồng bộ sang nhánh main...")
                        run_cmd("git merge dev --no-edit", ROOT_DIR)
                        code, _, err = run_cmd("git push origin main", ROOT_DIR)
                        if code == 0:
                            print("   ✅ Nhánh main trên GitHub đã cập nhật!")
                        else:
                            print(f"   ⚠️ Lỗi push main: {err}")

                        print(f"🎉 [HOÀN TẤT] GitHub đã đồng bộ 100% với máy tính!\n")
                        print("Tiếp tục lắng nghe thay đổi...")
                    else:
                        print("ℹ️ Không có thay đổi nào cần commit.")

                    pending_sync = False

            time.sleep(CHECK_INTERVAL_SECONDS)

        except KeyboardInterrupt:
            print("\nĐã dừng đồng bộ thời gian thực theo yêu cầu.")
            break
        except Exception as e:
            print(f"Lỗi: {e}")
            time.sleep(CHECK_INTERVAL_SECONDS)

if __name__ == "__main__":
    main()
