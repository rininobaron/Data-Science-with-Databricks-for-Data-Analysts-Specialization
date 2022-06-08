import os

files = os.listdir()

print(files)

for file in files:
    if file[-4:] == '.pdf':
        os.system('rm -rf ' + '"' + file + '"')