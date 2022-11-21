@setlocal enableextensions
@cd /d "%~dp0"
@Echo OFF


setlocal
for /f "tokens=2 delims=[]" %%i in ('ver') do set VERSION=%%i
for /f "tokens=2-3 delims=. " %%i in ("%VERSION%") do set VERSION=%%i.%%j
cd %~dp0%programs\windows 10
if "%VERSION%" == "6.1" cd %~dp0%programs\windows 7

if exist "%windir%\sysWOW64\" (
 start python-3.9.6-amd64
 start OpenVPN-2.5.3-I601-amd64.msi
) else (
  start OpenVPN-2.5.3-I601.msi
  start python-3.8.10
)
pause
python_installer.py
@cd /d %~dp0%\clicks\
if exist %USERPROFILE%\Desktop\clicker (
  copy *.* %USERPROFILE%\Desktop\clicker\
) else (
  mkdir %USERPROFILE%\Desktop\clicker
  copy *.* %USERPROFILE%\Desktop\clicker\
)
exit


