@echo off
REM Use the full path to python.exe and pytest module
pytest -v -s --html=.\Reports\report.html .\testCases\test_login.py .\testCases\test_profile.py .\testCases\test_jobsearch.py --browser firefox
REM Pause to keep the terminal window open after execution
pause