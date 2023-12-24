@echo off
echo Installing Python 3.10.9...
curl https://www.python.org/ftp/python/3.10.9/python-3.10.9-amd64.exe -o python-3.10.9-amd64.exe
start /wait python-3.10.9-amd64.exe /quiet InstallAllUsers=1 PrependPath=1
del python-3.10.9-amd64.exe

echo Installing discord.py...
python -m pip install discord.py

echo Installation complete.
