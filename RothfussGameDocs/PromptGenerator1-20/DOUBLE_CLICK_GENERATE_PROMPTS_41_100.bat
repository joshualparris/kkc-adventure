@echo off
setlocal

cd /d "%~dp0"
title KKC Prompt Generator

echo.
echo ==========================================
echo   KKC Prompt Generator: Prompts 41-100
echo ==========================================
echo.

if not exist "prompt_manifest_41_100.json" (
    echo Creating placeholder manifest for prompts 41-100...
    python create_prompt_manifest_skeleton.py --start 41 --end 100
    if errorlevel 1 goto :failed
) else (
    echo Using existing prompt_manifest_41_100.json
)

echo.
echo Validating manifest...
python validate_manifest.py --manifest prompt_manifest_41_100.json --start 41 --end 100
if errorlevel 1 goto :failed

echo.
echo Previewing prompts 41-43...
python generate_prompts.py --manifest prompt_manifest_41_100.json --start 41 --end 43 --dry-run
if errorlevel 1 goto :failed

echo.
echo Generating prompts 41-100...
python generate_prompts.py --manifest prompt_manifest_41_100.json --start 41 --end 100
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
