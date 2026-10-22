@echo off
title Realtime Git Sync (Worktree - GitHub)
chcp 65001 >nul
cd /d "%~dp0"
echo Khởi động tiến trình theo dõi và tự động đồng bộ thời gian thực...
python realtime_sync.py
pause
