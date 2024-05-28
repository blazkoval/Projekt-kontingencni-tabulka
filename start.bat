@echo off
powershell -NoExit -Command "& {Set-Location 'D:\projekt-kont-tabulka\Projekt-kontingencni-tabulka'; py transformData.py}"