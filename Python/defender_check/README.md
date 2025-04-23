# defender_check.py
A simple script to use on Windows to run on-demand scans using the AMSI  
API. This script only works on Windows due to the nature of the AMSI API.

## Virtual Environment Configuration
1. Setup a virtual environment for dependencies
```
python -m venv \path\to\new\virtual\environment\defender_check
```
2. Activate virtual environment
```
\path\to\new\virtual\environment\defender_check\scripts\activate.bat
```
3. Install requirements from requirements.txt within the virtual environment
```
python -m pip install -r requirements.txt
```

## Usage and Help Menu
```
usage: defender_check.py [options]

A simple script to compare a file or string against the AMSI engine.

options:
  -h, --help                                show this help message and exit
  -f FILE_NAME, --file FILE_NAME            File or file path to test.
  -s STRING_VALUE, --string STRING_VALUE    String to test.

by Blu3gl0w13 - April 23, 2025
```
