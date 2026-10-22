@echo off
title Go khoi dong cung Windows (Client Auto-Sync)
chcp 65001 >nul
echo ======================================================================
echo   HỦY CÀI ĐẶT TỰ KHỞI ĐỘNG CÙNG WINDOWS (MÁY CON)
echo ======================================================================
echo.
set "SHORTCUT_PATH=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\ClientAutoSync.lnk"

if exist "%SHORTCUT_PATH%" (
    del "%SHORTCUT_PATH%"
    echo [THÀNH CÔNG] Đã xóa khỏi thư mục Startup của Windows!
    echo Máy tính sẽ không tự chạy đồng bộ khi khởi động lại nữa.
) else (
    echo [THÔNG BÁO] Tính năng tự khởi động hiện chưa được cài đặt.
)

echo.
echo Đang tắt tiến trình đồng bộ ngầm đang chạy (nếu có)...
powershell -NoProfile -Command "Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -like '*client_realtime_pull.py*' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force; Write-Host ('Đã dừng tiến trình PID: ' + $_.ProcessId) }"

echo.
pause
