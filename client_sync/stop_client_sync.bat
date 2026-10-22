@echo off
chcp 65001 >nul
echo Đang tắt tiến trình nhận đồng bộ trên máy con...
powershell -NoProfile -Command "Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -like '*client_realtime_pull.py*' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force; Write-Host ('Đã dừng tiến trình PID: ' + $_.ProcessId) }"
echo Hoàn tất.
pause
