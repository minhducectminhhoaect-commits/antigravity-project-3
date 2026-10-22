@echo off
chcp 65001 >nul
echo ======================================================================
echo   ĐỒNG BỘ WORKTREE DEV LÊN GITHUB (KHÔNG THAY ĐỔI THƯ MỤC GỐC)
echo ======================================================================
cd /d "%~dp0"

echo [1/3] Quét toàn bộ thay đổi trong worktree dev...
git add -A

git diff --cached --quiet
if %ERRORLEVEL% EQU 0 (
    echo [INFO] Không có thay đổi nào mới trong worktree dev.
) else (
    echo [2/3] Đang commit các thay đổi (file thêm / xóa / chỉnh sửa)...
    git commit -m "Worktree dev sync: %DATE% %TIME%"
    echo [3/3] Đang đẩy lên GitHub nhánh dev...
    git push origin dev
    echo ======================================================================
    echo   HOÀN TẤT: Đã đẩy lên GitHub nhánh dev!
    echo   Lưu ý: Thư mục gốc D:\antigravity 3 hoàn toàn giữ nguyên độc lập.
    echo ======================================================================
)

echo.
pause
