@echo off

rem Change working dir
cd %~dp0

rem Create venv
python -m venv venv

rem Activate venv
call venv\Scripts\activate

rem Install requirements
pip install -r requirements.txt

rem Call robot script
python src\framework.py %1 %2 %3