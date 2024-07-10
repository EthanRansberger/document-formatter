@echo off
REM Check if the virtual environment exists
IF NOT EXIST "venv\Scripts\activate.bat" (
    echo Virtual environment not found. Please create a virtual environment first.
    pause
    exit /B 1
)

REM Activate the virtual environment
call venv\Scripts\activate.bat

REM Run the document formatter script and log errors
python src\markdown_to_formatted_docx.py 2>> error_log.txt

REM Deactivate the virtual environment
deactivate

REM Check if there were any errors and notify the user
IF %ERRORLEVEL% NEQ 0 (
    echo Errors were encountered during execution. Please check error_log.txt for details.
    pause
)
