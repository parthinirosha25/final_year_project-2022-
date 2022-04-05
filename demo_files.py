# searching files and folder in our desktop using python
import os
import glob

#target folder(read dir)
your_folder_path = r'D:\.'

# List of files (by last dir name)
list_of_files = os.listdir(your_folder_path)

# print all files and folders
print("\n----------------------------\n\nList of files and folder :")
print("\n---------------------------------- \n ")

for your_folder_path in list_of_files:
    print(your_folder_path)

print('\n ----------------------------------------------------------- \n')

#filter files by extension
print("Filter files by extension: \n")

for your_folder_path in list_of_files:
    if '.pdf' in your_folder_path:
        print(your_folder_path)
    elif '.*' in your_folder_path:
        print(your_folder_path)
    elif '.xlsx' in your_folder_path:
        print(your_folder_path)
    elif '.docx' in your_folder_path:
        print(your_folder_path)
    elif '.csv' in your_folder_path:
        print(your_folder_path)
    elif '.jpeg' in your_folder_path:
        print(your_folder_path)
    elif '.PNG' in your_folder_path:
        print(your_folder_path)
    elif '.html' in your_folder_path:
        print(your_folder_path)
    elif '.js' in your_folder_path:
        print(your_folder_path)
    elif '.py' in your_folder_path:
        print(your_folder_path)
    elif '.css' in your_folder_path:
        print(your_folder_path)
    elif '.txt' in your_folder_path:
        print(your_folder_path)
    elif '.json' in your_folder_path:
        print(your_folder_path)
    elif '.md' in your_folder_path:
        print(your_folder_path)
    elif '.ejs' in your_folder_path:
        print(your_folder_path)
    elif '.d.ts' in your_folder_path:
        print(your_folder_path)
    elif '.ejs' in your_folder_path:
        print(your_folder_path)
    elif '.pdf' in your_folder_path:
        print(your_folder_path)
    elif '.lnk' in your_folder_path:
        print(your_folder_path)
    else:
        print('input invalid')

print('\n ----------------------------------------------------------- \n')

# OS WALK function will gives 3 elements (all roots, all sub dirs (or) sub folders and files)
# ------------------------------------------------------------------------------------------

# directory = r'D:\.'
#
# for root, subdirectories, files in os.walk(directory):
#     for subdirectory in subdirectories:
#         print(os.path.join(root, subdirectory))
#     for file in files:
#         print(os.path.join(root, file))


print('\n ----------------------------------------------------------- \n')

# search a keyword from different txt files in a folder and return the filename (python).
# ----------------------------------------------------------------------------------------



