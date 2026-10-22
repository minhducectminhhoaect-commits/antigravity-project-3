@echo off
chcp 65001 >nul
echo ======================================================================
echo   ĐỒNG BỘ WORKTREE DEV LÊN GITHUB (THÊM / SỬA / XÓA FILE)
echo ======================================================================
cd /d "%~dp0"

echo [1/4] Quét toàn bộ thay đổi trong worktree dev...
git add -A

git diff --cached --quiet
if %ERRORLEVEL% EQU 0 (
    echo [INFO] Không có thay đổi nào mới trong worktree dev.
) else (
    echo [2/4] Đang commit các thay đổi (file thêm / xóa / chỉnh sửa)...
    git commit -m "Sync: cap nhat tu worktree dev (%DATE% %TIME%)"
    echo [3/4] Đang đẩy lên GitHub nhánh dev...
    git push origin dev
    echo [OK] Đã đẩy thành công lên nhánh dev trên GitHub!
)

echo.
echo [4/4] Đồng bộ sang nhánh main của thư mục gốc và đẩy lên GitHub...
cd /d "%~dp0..\.."
git merge dev --no-edit
git push origin main

echo.
echo ======================================================================
echo   HOÀN TẤT: Toàn bộ GitHub (nhánh dev ^& main) đã giống 100%% với máy!
echo   - File trên máy xóa  -^> Trên GitHub cũng bị xóa
echo   - File trên máy thêm -^> Trên GitHub cũng được thêm
echo ======================================================================
echo.
pause
