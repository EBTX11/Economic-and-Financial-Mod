@echo off
node -v > nul 2>&1
IF %ERRORLEVEL% EQU 0 (
    start cmd.exe /k "node app.js"
) ELSE (
    echo Node.js is not installed. Please install Node.js and try again.
    pause
)
