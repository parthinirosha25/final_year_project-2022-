# import required module for speech recognition
import pyttsx3
import os
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

print("")
print("    My name is Nirosha,I make this tool With this help of tool you can open below things.......")

print("\n\t \t 1.FILE EXPLORER   \n\n\t\t 0. FOR EXIT")

print("\n    (YOU CAN USE NUMBER (OR) YOU CAN DO CHAT LIKE 'FILE EXPLORER' etc....)")

print(
    "\n  ============================================ Welcome To My Digital voice Assistant tool ============================================")
pyttsx3.speak("Welcome to my Digital voice Assistant")
print("")
print("")

pyttsx3.speak("chat with me with your requirements or you can speak with me ")

while True:
    # take input
    print("    CHAT WITH ME WITH YOUR REQUIREMENTS (or) ", end='')
    # p = input()
    # p = p.upper()
    # print(p)

    with sr.Microphone() as source:
        print("Speak Anything ")
        print("\n ---------------------------------- ")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            p = text.upper()
            print(" \n\t     You said : {}".format(p))

        except:
            print("\n Sorry could not recognize what you said")

    print("\n--------------------------------- ")

    if ("DONT" in p) or ("DON'T" in p) or ("NOT" in p):
        pyttsx3.speak("Type Again")
        print(".")
        print(".")
        continue

    # assignements for file explorer
    elif ("FILES" in p) or ("FILE EXPLORER" in p) or ("EXPLORER" in p) or ("FILE" in p) or ("DRIVE" in p) or ("1" in p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("FILE EXPLORER")
        print(".")
        print(".")
        os.system("explorer")

    # close the program
    elif ("EXIT" in p) or ("QUIT" in p) or ("CLOSE" in p) or ("0" in p):
        pyttsx3.speak("Exiting")
        break

    # for invalid input
    else:
        pyttsx3.speak(p)
        print("Is Invalid Input,Please Try Again")
        pyttsx3.speak("is Invalid,Please try again")
        print(".")
        print(".")

# we should import all library function used in this program