@echo off
cd %~dp0
cd ../../../
set FILEPATH=docs\FILETREE.md

:: Check if the file exists and delete it
if exist %FILEPATH% (
    del %FILEPATH%
)

:: Create the file tree and save it to FILETREE.md
tree /F > %FILEPATH%

echo File tree updated in %FILEPATH%
