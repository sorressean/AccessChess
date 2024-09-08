@echo off
del /s /q main.build output main.dist
nuitka --standalone --prefer-source-code main.pyw
iscc setup.iss
