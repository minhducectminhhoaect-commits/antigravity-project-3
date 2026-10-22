@echo off
chcp 65001 >nul
echo ========================================================
echo   ĐỒNG BỘ WORKTREE DEV LÊN GITHUB (THÊM / SỬA / XÓA)
echo ========================================================
cd /d "%~dp0"

echo [1/3] Quét tất cả thay đổi (thêm mới, chỉnh sửa, xóa file)...
git add -A

git diff --cached --quiet
if %ERRORLEVEL% EQU 0 (
    echo [INFO] Không có thay đổi nào mới để đồng bộ.
) else (
    echo [2/3] Đang tạo commit ghi nhận thay đổi...
    git commit -m "Sync worktree dev: %DATE% %TIME%"
    echo [3/3] Đang đẩy lên GitHub nhánh dev...
    git push origin dev
    echo ========================================================
    echo [THÀNH CÔNG] GitHub nhánh dev đã cập nhật 100%% theo máy!
    echo ========================================================
)

echo.
pause
