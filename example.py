# searching files and folder in our desktop using python
import os
import glob
import pathlib
import itertools

# import required module for speech recognition
import pyttsx3
import speech_recognition as sr

# voice driver code
r = sr.Recognizer()

# create object and assign voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# changing index changes voices but only [ 0(Male) and 1(Female) are working here ]
engine.setProperty('voice', voices[1].id)
engine.runAndWait()
print("")
print("")

# introduction
print("  =============================================== Digital voice Assistant tool!! ================================================")
engine.say('Hi, Its really good to hear from you!.....')

# ---------------------------------------------------------------
# sample running code for searching files and folders =====> (5)
# ---------------------------------------------------------------

pyttsx3.speak("  This tool will help you to find files in our desktop ")
print(" ")
pyttsx3.speak("  Please Enter file name that you want to open ")
print(" ")
n1 = input("Input the Filename: ")

# ----------------------------------------------
# input from user through voice
# ----------------------------------------------
# while True:
#     # take input from user through voice as input
#     print("\n CHAT WITH ME WITH YOUR REQUIREMENTS (or) ", end='')
#
#     with sr.Microphone() as source:
#         print("Speak Something ")
#         print("\n ---------------------------------- ")
#         audio = r.listen(source)
#         try:
#             text = r.recognize_google(audio)
#             p = text.lower()
#             print(" \n\t You said : {}".format(p))
#
#         except:
#             print("\n Sorry could not recognize what you said")
#
#     print("\n------------------------------------ \n")
#     break

list_all_ext = [x+y for x in [n1] for y in ['.php', '.cpp', '.jpeg', '.mp3', '.docx', '.pdf', '.xlsx', '.pptx', '.py',
                                            '.java', '.css', '.html', '.js', '.json']]
print(list_all_ext)
print(type(list_all_ext))

# this code will search available files in the D:\ drive
def find_files(filename, search_path):
   result = []

# Wlaking top-down from the root
   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
      # else:
      #    print("\n not found ....... \n")
   return result

print("\n =========================== Here Matching Result ==============================")
print("")
pyttsx3.speak("  Here the Matching results are  ")

# for i in list_all_ext:
#    print(find_files(i,"D:\."))            // to print simple value with [] empty list
count1 = 0
count2 = 0

# this loop for [D:\.] disk
for i in list_all_ext:
   if (find_files(i, "D:\.") != []):
      print(find_files(i, "D:\."))
   elif (find_files(i, "D:\.") == []):
      a = False
      count1 = count1 + 1
      pass
   else:
      pass     # pass comment is used to not print any value and simply blank

# this loop for [E:\.] disk
for i in list_all_ext:
   if (find_files(i, "E:\.") != []):
      print(find_files(i, "E:\."))
   elif (find_files(i, "E:\.") == []):
      a = False
      count2 = count2 + 1
      pass
   else:
      pass     # pass comment is used to not print any value and simply blank

if (count1 == len(list_all_ext) and count2 == len(list_all_ext)):
   # print(count1)
   # print(count2)
   print("\n No Matching Results Found")
   print("\n =========================== No Matching Result found ==============================")
   print("")
   pyttsx3.speak("  Sorry! No Matching results found. please give a valid input")

# # this loop for [C:\.] disk
# for i in list_all_ext:
#    if (find_files(i, "C:\.") != []):
#       print(find_files(i, "C:\."))
#    elif (find_files(i, "C:\.") == []):
#       a = False
#       count = count+1
#       pass
#    else:
#       pass     # pass comment is used to not print any value and simply blank

# if (count == len(list_all_ext)):
#    print(count)
#    print("\n No Matching Results Found")
#    print("\n =========================== No Matching Result found ==============================")
#    print("")
#    pyttsx3.speak("  Sorry! No Matching results found. please give a valid input")

# #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# # this code will print input value + extension in a single list ====> (5)
# --------------------------------------------------------------------
# list_all_ext = [x+y for x in [n1] for y in ['.php', '.cpp', '.jpeg', '.mp3', '.docx', '.pdf', '.xlsx', '.pptx', '.py',
#                                             '.java', '.css', '.html', '.js', '.json']]
# print(list_all_ext)
# print(type(list_all_ext))
# #
# # this code will search available files in the D:\ drive
# def find_files(filename, search_path):
#    result = []
#
# # Wlaking top-down from the root
#    for root, dir, files in os.walk(search_path):
#       if filename in files:
#          result.append(os.path.join(root, filename))
#       # else:
#       #    print("\n not found ....... \n")
#    return result
#
# print(" =========================== Here Matching Result ==============================")
# print("")
# pyttsx3.speak("  Here the Matching results are  ")
#
# # for i in list_all_ext:
# #    print(find_files(i,"D:\."))            // to print simple value with [] empty list
# count = 0
#
# # this loop for [D:\.] disk
# for i in list_all_ext:
#    if (find_files(i, "D:\.") != []):
#       print(find_files(i, "D:\."))
#    elif (find_files(i, "D:\.") == []):
#       a = False
#       count = count+1
#       pass
#    else:
#       pass     # pass comment is used to not print any value and simply blank
#
# # this loop for [E:\.] disk
# for i in list_all_ext:
#    if (find_files(i, "E:\.") != []):
#       print(find_files(i, "E:\."))
#    elif (find_files(i, "E:\.") == []):
#       a = False
#       count = count+1
#       pass
#    else:
#       pass     # pass comment is used to not print any value and simply blank

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# # this loop for [C:\.] disk
# for i in list_all_ext:
#    if (find_files(i, "C:\.") != []):
#       print(find_files(i, "C:\."))
#    elif (find_files(i, "C:\.") == []):
#       a = False
#       count = count+1
#       pass
#    else:
#       pass     # pass comment is used to not print any value and simply blank

# if (count == len(list_all_ext)):
#    print(count)
#    print("\n No Matching Results Found")
#    print("\n =========================== No Matching Result found ==============================")
#    print("")
#    pyttsx3.speak("  Sorry! No Matching results found. please give a valid input")

# ----------------------------------------------------------------------
# for i in list_all_ext:
#    if (find_files(i, "D:\.") != []):                     # this if statement for D:\. disk
#       print(find_files(i, "D:\."))
#    elif (find_files(i, "C:\.") != []):                   # this if statement for C:\. disk
#       print(find_files(i, "C:\."))
#    elif (find_files(i, "E:\.") != []):                   # this if statement for E:\. disk
#       print(find_files(i, "E:\."))
#    elif (find_files(i, "D:\.") == []):
#       a = False
#       count = count+1
#       pass
#    elif (find_files(i, "C:\.") == []):                  # this if statement for C:\. disk
#       a = False
#       count = count + 1
#       pass
#    elif (find_files(i, "E:\.") == []):                  # this if statement for E:\. disk
#       a = False
#       count = count + 1
#       pass
#    else:
#       pass     # pass comment is used to not print any value and simply blank



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ['.swift', '.vb', '.sys', '.tmp', '.min.css', '.bundle.min.js', '.bootstrap.min.*',
#                                             '.bootstrap', '.asp', '.php', '.rss', '.pps', '.cpp', '.c', '.cs', '.h',
#                                            '.xml', '.email', '.pl', '.com', '.jar', '.msi', '.ico', '.svg',
#                                             '.mp3', '.pkg', '.rar', '.bin', '.dat', '.db', '.mdb', '.sql',
#                                             '.GIF', '.MID', '.PPT', '.PPTX', '.PNG', '.PSD', '.TIF', '.TXT',
#                                             '.ZIP', '.CSV', '.CLASS', '.BMP', '.jdk', '.EXE' , '.MAP', '.AU',
#                                             '.BAT', '.AVI', '.CSV']
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ----------------------------------------------------------------
# sample running code for searching files and folders =====> (4)
# ----------------------------------------------------------------

# f_extns = n1.split(".")
# n2 = repr(f_extns[-2])
# print ("File : " + n2)
# i = 0
# j = 1
# b1 = 0

# list_of_ext = ['.docx', '.xlsx', '.pptx', '.py', '.java', '.css', '.html', '.js', '.json']

# for i in range(0,len(list_of_ext)):
#    b1 = (n1+list_of_ext[i]).split()
#    print(i)
#    print(b1)
#    print(type(b1))


# sample running code for searching files and folders =====> (3)
# ---------------------------------------------------------------

# n1 = input("Input the Filename: ")
# # f_extns = n1.split(".")
# # n2 = repr(f_extns[-2])
# # print ("File : " + n2)
#
# def find_files(filename, search_path):
#    result = []
#
# # Wlaking top-down from the root
#    for root, dir, files in os.walk(search_path):
#       if filename in files:
#          result.append(os.path.join(root, filename))
#    return result
#
# print(find_files(n1,"D:\."))

# os.system("explorer")


# OS WALK function will gives 3 elements (all roots, all sub dirs (or) sub folders and files)
# ------------------------------------------------------------------------------------------
# sample running code for searching files and folders =====> (2)
# ---------------------------------------------------------------

# directory = r'D:\.'
# FOLDER_PATH = r'D:\.'
#
# print('\n ************************************************\n')
#
# def listDir(dir):
#     fileNames = os.listdir(dir)
#     for fileName in fileNames:
#         print('File Name: '+fileName)
#         for root, subdirectories, files in os.walk(directory):
#             for subdirectory in subdirectories:
#                 a = os.path.join(root, subdirectory)
#                 last1 = os.listdir(a)
#                 # print(last1)
#                 a1 = os.path.abspath(os.path.join(a,fileName))
#                 print("-------------------------------------------------------\n")
#                 print("path 1 : "+a1)
#                 print(last1)
#                 print("-------------------------------------------------------\n")
#                 # print(os.path.join(root, subdirectory))
#             for file in files:
#                 b = os.path.join(root, file)
#                 last2 = os.listdir(b)
#                 # print(last2)
#                 b1 = os.path.abspath(os.path.join(b, fileName))
#                 print("-------------------------------------------------------\n")
#                 print("path 2 : "+b1)
#                 print(last2)
#                 # print(os.path.join(root, file))
#                 print("-------------------------------------------------------\n")
#
#     for fileName in fileNames:
#         print('File Name: '+fileName)
#         print('\n Folder Path: '+os.path.abspath(os.path.join(dir,fileName)),sep='\n')
#         # print('\n All Sub Folder Path(1): ' + os.path.abspath(os.path.join(root, subdirectory)), sep='\n')
#         # print('\n All Sub Folder Path(2): ' + os.path.abspath(os.path.join(root, file)), sep='\n')
#         print('\n ************************************************\n')
#
# if __name__ == '__main__':
#     listDir(FOLDER_PATH)


# -------------------------------------------------
# list_of_files = os.listdir(your_folder_path)
#-------------------------------------------------

# for root, subdirectories, files in os.walk(directory):
#     for subdirectory in subdirectories:
#         a = os.path.join(root, subdirectory)
#         a1 = os.path.basename(a)
#         print(a1)
#         if(filename == a1):
#             print("true 1")
#         # print(os.path.basename(a1))
#     for file in files:
#         b = os.path.join(root, file)
#         b1 = os.path.basename(b)
#         print(b1)
#         if (filename == b1):
#             print("true 2")
#         # print(os.path.basename(b))

print('\n ************************************************\n')


# for filename in base1:
#     for filename in base2:
#         if(filename == os.path.basename(a)):
#            print("\n true ma \n")
#            print(os.path.join(root, subdirectory))
#            print(os.path.basename(a))
#         else:
#            print("\n true pa \n")
#            print(os.path.join(root, subdirectory))
#            print(os.path.basename(a))


# c = os.path.basename(a);
# filename = input("Input the Filename: ")
# f_extns = filename.split(".")
# print ("The extension of the file is : " + repr(f_extns[-2]))
print('\n ************************************************\n')


