
@ECHO OFF

SET BatFileName=%~n0
SET JobName=%BatFileName:~0,8%
SET JobName2=MAF00200

d:
cd User_Application\%JobName%
call venv\Scripts\activate
start "%JobName%" python manage.py runserver
start code d:\User_Application\%JobName%

cd ..
cd %JobName2%
start "frontend" npm run serve
start /b code -n d:\User_Application\%JobName2% 

