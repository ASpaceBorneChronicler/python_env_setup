@echo off

:: Check if the user provided a filename (directory name)
if "%1"=="" (
    echo Please provide the project name as a parameter.
    exit /b 1
)

:: Set the directory name from the first argument
set PROJECT_NAME=%1

:: Run the Python script and pass the project name as an argument
python "C:\Users\ADMIN\Documents\Python Scripts\python_automation\setup_venv.py" %PROJECT_NAME%
