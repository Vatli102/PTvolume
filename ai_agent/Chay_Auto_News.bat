@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo =========================================================
echo    DANG QUET TIN TUC QUOC TE & DANG BAI LEN PTVOLUME.COM
echo =========================================================
py auto_news_publisher.py
pause
