@echo off
title Cai dat khoi dong cung Windows (Client Auto-Sync)
chcp 65001 >nul
echo ======================================================================
echo   CÀI ĐẶT TỰ ĐỘNG ĐỒNG BỘ CÙNG KHỞI ĐỘNG WINDOWS (MÁY CON)
echo ======================================================================
echo.
set "TARGET_DIR=%~dp0"
set "VBS_PATH=%TARGET_DIR%start_client_sync_background.vbs"
set "STARTUP_DIR=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
set "SHORTCUT_PATH=%STARTUP_DIR%\ClientAutoSync.lnk"

powershell -NoProfile -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('%SHORTCUT_PATH%'); $s.TargetPath = '%VBS_PATH%'; $s.WorkingDirectory = '%TARGET_DIR%'; $s.Description = 'Tu dong nhan dong bo Git Client'; $s.Save()"

if exist "%SHORTCUT_PATH%" (
    echo [THÀNH CÔNG] Đã thêm vào thư mục Startup của Windows!
    echo.
    echo Từ nay, mỗi khi máy tính này khởi động hoặc đăng nhập lại:
    echo  - Tiến trình đồng bộ sẽ TỰ ĐỘNG CHẠY NGẦM.
    echo  - Luôn luôn giữ thư mục khớp 100%% với máy chủ Master.
    echo  - Bạn không cần phải mở file thủ công nữa.
    echo.
    echo Đang khởi chạy tiến trình đồng bộ ngay bây giờ...
    wscript "%VBS_PATH%"
) else (
    echo [LỖI] Không thể tạo shortcut khởi động. Vui lòng kiểm tra quyền truy cập.
)

echo.
pause
