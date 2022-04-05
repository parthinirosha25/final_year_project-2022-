# searching files and folder in our desktop using python
import os
import glob
import pathlib

# OS WALK function will gives 3 elements (all roots, all sub dirs (or) sub folders and files)
# ------------------------------------------------------------------------------------------
# sample running code for searching files and folders
# --------------------------------------------------

directory = r'D:\.'
FOLDER_PATH = r'D:\.'

print('\n ************************************************\n')

def listDir(dir):
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        print('File Name: '+fileName)
        for root, subdirectories, files in os.walk(directory):
            for subdirectory in subdirectories:
                a = os.path.join(root, subdirectory)
                last1 = os.listdir(a)
                # print(last1)
                a1 = os.path.abspath(os.path.join(a,fileName))
                print("-------------------------------------------------------\n")
                print("path 1 : "+a1)
                print(last1)
                print("-------------------------------------------------------\n")
                # print(os.path.join(root, subdirectory))
            for file in files:
                b = os.path.join(root, file)
                last2 = os.listdir(b)
                # print(last2)
                b1 = os.path.abspath(os.path.join(b, fileName))
                print("-------------------------------------------------------\n")
                print("path 2 : "+b1)
                print(last2)
                # print(os.path.join(root, file))
                print("-------------------------------------------------------\n")

    for fileName in fileNames:
        print('File Name: '+fileName)
        print('\n Folder Path: '+os.path.abspath(os.path.join(dir,fileName)),sep='\n')
        # print('\n All Sub Folder Path(1): ' + os.path.abspath(os.path.join(root, subdirectory)), sep='\n')
        # print('\n All Sub Folder Path(2): ' + os.path.abspath(os.path.join(root, file)), sep='\n')
        print('\n ************************************************\n')

if __name__ == '__main__':
    listDir(FOLDER_PATH)