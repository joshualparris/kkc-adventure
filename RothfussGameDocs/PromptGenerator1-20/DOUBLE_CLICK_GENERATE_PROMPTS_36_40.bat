@echo off
setlocal

cd /d "%~dp0"
title KKC Prompt Generator

echo.
echo ==========================================
echo   KKC Prompt Generator: Prompts 36-40
echo ==========================================
echo.
echo Validating manifest...
python validate_manifest.py --start 21 --end 40
if errorlevel 1 goto :failed

echo.
echo Previewing prompts 36-38...
python generate_prompts.py --start 36 --end 38 --dry-run
if errorlevel 1 goto :failed

echo.
echo Generating prompts 36-40...
python generate_prompts.py --start 36 --end 40
if errorlevel 1 goto :failed

echo.
echo Opening generated_prompts folder...
start "" "%~dp0generated_prompts"

echo.
echo Finished successfully.
echo.
pause
exit /b 0

:failed
echo.
echo Something went wrong. Scroll up to see the error.
echo.
pause
exit /b 1
