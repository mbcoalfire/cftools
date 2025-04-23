#defender_check.py
A simple script to use on Windows to run on-demand scans using the AMSI  
API. This script only works on Windows due to the nature of the AMSI API.

##Virtual Environment Configuration
```
python -m venv \path\to\new\virtual\environment\defender_check
\path\to\new\virtual\environment\defender_check\scripts\activate.bat
python -m pip install -r requirements.txt
```

##Usage and Help Menu
```
usage: defender_check.py [options]

A simple script to compare a file or string against the AMSI engine.

options:
  -h, --help                                show this help message and exit
  -f FILE_NAME, --file FILE_NAME            File or file path to test.
  -s STRING_VALUE, --string STRING_VALUE    String to test.

by Blu3gl0w13 - April 23, 2025
```
