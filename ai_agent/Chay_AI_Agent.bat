@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo ===================================================
echo     DANG KHOI CHAY AI TRADING AGENT (VSA & WYCKOFF)
echo ===================================================
py trading_agent.py
pause
