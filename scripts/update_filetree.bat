@echo off
REM Navigate to the directory of the batch file
cd %~dp0
REM Navigate up three directories to the repository root
cd ../
echo Current directory: %cd%
pause 
REM Set the file path for the file tree document
set FILEPATH=docs\FILETREE.md

REM Check if the file exists and delete it if it does
if exist %FILEPATH% (
    del %FILEPATH%
    echo found existing and deled
    pause
)

REM Create the file tree and append it to FILETREE.md
tree /F >> %FILEPATH%
echo tree /F >> %FILEPATH%
pause
REM Print a confirmation message
echo File tree updated in %FILEPATH%
pause
