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

for path in os.walk(target_path):
    #print(path[0])
    if path[0][87:91] != '.git':
        #print(path[0])
        directories.append(path[0])

# Remove unnecessary directories 
directories.remove(directories[0])                  # FIRST ELEMENT
directories.remove(directories[0])                  # FIRST ELEMENT AGAIN
directories.remove(directories[len(directories)-1]) # LAST ELEMENT
# print()
# for i in directories:
#     print(i)

for path in directories:
    print()
    files = os.listdir(path)
    for file in files:
        path_file = path + '/' + file
        print(path_file)
        if file[-5:] == '.html':
            HTML(path_file).write_pdf(file[:-5] + '.pdf', stylesheets=[css])