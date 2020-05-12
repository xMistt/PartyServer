@echo off
ECHO Installing the required packages for the server!
TIMEOUT 3

set SANIC_NO_UVLOOP=true
set SANIC_NO_UJSON=true
py -3 -m pip install -U -r requirements.txt

ECHO Done! Now run START SERVER.bat
PAUSE
