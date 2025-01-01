@echo off
::----------------------------------------
:: Name: SearchBaseDatasetConfig.bat
::----------------------------------------
:: Description:
::   This script searches for the string "BaseDatasetConfig" in all files 
::   within the specified directory (including subfolders).
::
:: Usage:
::   1. Update the "TARGET_FOLDER" path below or pass it as an argument.
::   2. Run this .bat file to see which files contain the target string.
::
:: Example:
::   SearchBaseDatasetConfig.bat "C:\MyProject\src"
::----------------------------------------

REM If a folder path is provided as an argument, use that. Otherwise, use a default folder.
IF NOT "%~1"=="" (
    SET "TARGET_FOLDER=%~1"
) ELSE (
    SET "TARGET_FOLDER=C:\Users\trigg\Documents\GitHub\greg-ai"
)

echo.
echo Searching for "BaseDatasetConfig" in %TARGET_FOLDER% ...
echo.

REM /S  = Search in subfolders
REM /I  = Case-insensitive search
REM /M  = Print only the filenames that match
REM *.* = All files
findstr /S /I /M "BaseDatasetConfig" "%TARGET_FOLDER%\*.*"

echo.
echo Done!
pause
