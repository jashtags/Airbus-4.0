import os
import sys
import fileinput

cwd = os.getcwd()
path="/Users/jashtanukonda/firstdjangoproj/firstdjangoproj/"
os.chdir(path)

with open('settings.py', 'r') as file :
    filedata = file.read()
filedata = filedata.replace('djongo', 'changed ')
with open('settings.py', 'w') as file:
    file.write(filedata)