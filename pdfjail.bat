@echo off
setlocal

:: Check for the correct number of parameters
if "%~1"=="" (
    echo Usage: pdfjail PASSWORD
    exit /b 1
)

:: Set password and directory based on parameters
set "password=%~1"
set "directory=%cd%"

set scriptDir=%~dp0
cd /d "%scriptDir%"
:: Run the Python script with the provided arguments
python pdfjail.py "%password%" "%directory%"

endlocal
