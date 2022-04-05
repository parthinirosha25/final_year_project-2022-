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
# n1 = input("Input the Filename: ")

# ----------------------------------------------
# input from user through voice
# ----------------------------------------------
while True:
    # take input from user through voice as input
    print("\n CHAT WITH ME WITH YOUR REQUIREMENTS (or) ", end='')

    with sr.Microphone() as source:
        print("Speak Something ")
        print("\n ---------------------------------- ")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            p = text.lower()
            print(" \n\t You said : {}".format(p))

        except:
            print("\n Sorry could not recognize what you said")

    print("\n------------------------------------ \n")
    break

list_all_ext = [x+y for x in [p] for y in ['.php', '.cpp', '.jpeg', '.mp3', '.docx', '.pdf', '.xlsx', '.pptx', '.py',
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

if (count1 == len(list_all_ext) and count2 == len(list_all_ext)):
   # print(count1)
   # print(count2)
   print("\n No Matching Results Found")
   print("\n =========================== No Matching Result found ==============================")
   print("")
   pyttsx3.speak("  Sorry! No Matching results found. please give a valid input")

print('\n ************************************************\n')
print('\n ************************************************\n')