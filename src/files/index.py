import os.path
from pathlib import Path

# to support both Windows and Linux
filePath = Path('./src/files/aFile.txt')

# read mode is defeault
with open(filePath, mode='a+') as myfile:
  if (os.stat(filePath).st_size < 50):
    myfile.write('Hi there\n')
 
  # reset the cursor to the first char
  myfile.seek(0)
  lines = myfile.readlines()
  print(lines)