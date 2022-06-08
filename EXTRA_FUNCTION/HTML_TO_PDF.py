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

 
rootdir = os.getcwd()
counter_not_git = 0
counter_target_paths = 0
for path in os.walk(rootdir):
    if path[0][87:91] != '.git':
        counter_not_git += 1
        if counter_not_git == 0:
            pass
        elif path[0][87:101] == 'EXTRA_FUNCTION':
            pass
        elif path[0].is_dir():
            counter_target_paths += 1
            print(path[0])
    # if path[1].is_dir():
    #     print(path)

# for path in directories:
#     files = os.listdir(path)
#     if file[-5:] == '.html':
#         HTML(i).write_pdf(i[:-5] + '.pdf', stylesheets=[css])