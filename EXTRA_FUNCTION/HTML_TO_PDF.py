from weasyprint import HTML, CSS
import os

'''
Search in all directories all files with 
.html and converts in pdf files
in PATHS and

'''

# Define sheet style using weasyprint.CSS() method
css = CSS(string='''
    @page {size: A4; margin: 1cm;} 
    th, td {border: 1px solid black;}
    ''')

# Get current working path
current_path = os.getcwd()

# 
target_path = current_path[:-15]

directories = []

print(directories)

for i in 

from pathlib import Path
import os
 
rootdir = os.getcwd()
for path in Path(rootdir).iterdir():
    if path.is_dir() and :
        print(path)

# for path in directories:
#     files = os.listdir(path)
#     if file[-5:] == '.html':
#         HTML(i).write_pdf(i[:-5] + '.pdf', stylesheets=[css])