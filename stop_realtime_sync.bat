@echo off
chcp 65001 >nul
echo Đang tắt tiến trình tự động đồng bộ thời gian thực...
powershell -Command "Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -like '*realtime_sync.py*' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force; Write-Host ('Đã dừng tiến trình PID: ' + $_.ProcessId) }"
echo Hoàn tất.
pause
