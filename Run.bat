@echo off

if [%1] == [] goto A
set n=%1
goto B

:A
echo Enter py File (e.g. MyCodeMaze.py): 
set /p n=
goto B

:B
python Minecraft.py %n%.py
