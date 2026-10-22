@echo off
title Client Auto-Sync (Nhan cap nhat tu GitHub)
chcp 65001 >nul
cd /d "%~dp0"
echo ======================================================================
echo   BẮT ĐẦU ĐỒNG BỘ MÁY CON (CHỈ NHẬN DỮ LIỆU - KHÔNG SỬA)
echo ======================================================================
python client_realtime_pull.py
pause
