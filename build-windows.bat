@echo off
del /s /q main.build output main.dist
nuitka --standalone --prefer-source-code --assume-yes-for-downloads --clang --lto=yes --windows-console-mode=disable main.py
iscc setup.iss
