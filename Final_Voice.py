''' desktop application for searching files and folders
    ===================================================  '''

# package used
import os
import pickle
import PySimpleGUI as sg
# sg.ChangeLookAndFeel('Dark')     # clr the output screen
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

    print("\n------------------------------------- \n")
    break

class Gui:    #class for GUI
    def __init__(self):     # create 2 obj is layout and window
        # layout contails all rows content in the list format (text box, input box, voice icon, radio button, buttons, etc)
        self.layout = [[sg.Text('Search Term', size=(10,1)),
                        sg.Input(size=(45,1), focus=True, key="TERM"),               #input box1
                        sg.Radio('Contains', group_id='choice', key="CONTAINS", default=True),         # keyword radio btn
                        sg.Radio('StartsWith', group_id='choice', key="STARTSWITH"),
                        sg.Radio('EndsWith', group_id='choice', key="ENDSWITH")],
                        [sg.Text('Root Path', size=(10,1)),
                         sg.Input('C:/', size=(45,1), key="PATH"),                          #input box2
                         sg.FolderBrowse('Browse'),                      #browse dir path
                         sg.Button('Re-Index', size=(10,1), key="_INDEX_"),              # indexing method
                         sg.Button('Search', size=(10,1), bind_return_key=True, key="_SEARCH_")],      # bind_return_key=True(if we press etr key this btn will trigger
                        [sg.Button('Speak',size=(9,1), key="SPEAK"),
                         sg.Input(size=(45,2))],
                        [sg.Output(size=(100,30))]]                       #size of the output screen

        self.window = sg.Window('Quick File Search').Layout(self.layout)

# search_engine class to init file indexing values
class SearchEngine:
    def __init__(self):                           # to init all file index values ( using os.walk() )
        self.file_index = []                      # init list of file directory index
        self.results = []                         # results will be stored in list
        self.matches = 0                          # count of the matching search and results
        self.records = 0                          # count

    # def create_new_index(self, root_path):
        ''' Create a new index and save to files ( here 2 method is used )
            1) create a new index
            2) save the index value ( C:\ -->  D:\ )
        '''

    def create_new_index(self, values):
        root_path = values['PATH']
        # here 'if files' comments is used to filter the empty file list
        self.file_index = [(root, files) for root, dirs, files in os.walk(root_path) if files]

        # save the index
        with open('file_index.pkl','wb') as f:      # open binary format writing files
            pickle.dump(self.file_index, f)         # save new index

    # Speak button function
    def speak_now(self, values):
        speak_value = values['SPEAK']

    def load_existing_index(self):
        ''' load existing index values (no need to create new index again and again ) '''

        # load the previous index value (using read method)
        try:
            with open('file_index.pkl','rb') as f:      # open binary format reading files
                self.file_index = pickle.load(f)
        except:
            self.file_index = []

    # def search(self, term, search_type = "contains"):          # here I was directly indexing the search value
        ''' this method will give which type of search that we used in GUI '''

    def search(self, values):
        # reset variables
        self.results.clear()
        self.matches = 0
        self.records = 0
        term = values['TERM']

        # perform search (each row in the file index)
        for path, files in self.file_index:
            for file in files:           # each file in the list of file
                self.records +=1      # iter record(files) search count
                '''by default search type is contains(keyword) and other search type such as (
                three scenario search
                1) contains(keyword)
                2) starts With
                3) Ends with 
                any of these condition is true respective file name with path will display  bool values
                 will return only true or false so by pass the values will give result'''
                # if(search_type == 'CONTAINS' and term.lower() in file.lower() or
                #    search_type == 'STARTSWITH' and file.lower().startswith(term.lower()) or
                #    search_type == 'ENDSWITH' and file.lower().endswith(term.lower())):

                if (values['CONTAINS'] and term.lower() in file.lower() or
                        values['STARTSWITH'] and file.lower().startswith(term.lower()) or
                        values['ENDSWITH'] and file.lower().endswith(term.lower())):

                    # result will be print in the format C:\ --> C:/ bcoz os.walk function will return backslash (\)
                    result = path.replace('\\','/') + '/' + file
                    self.results.append(result)     # append or add matching results
                    self.matches += 1               # matching count
                else:
                    continue

        # save search results to file (list of results, saving in txt file)
        with open('search_results.txt', 'w') as f:
            for row in self.results:
                f.write(row + '\n')

# --------------------------------------
# test funtion to check the output value
# def test1():
#     s = SearchEngine()    # call search engine class obj
#     # s.create_new_index('C:/')
#     s.load_existing_index()
#     s.search('RESUME')     # call function search
#
#     # to print the matching result in the variable using string variable format
#     print()
#     print('>> There were {:,d} matches out of {:,d} records searched.'.format(s.matches, s.records))
#     print()
#     print('>> This query produced the following matches: \n')
#     # iter the result and print those result in the screen
#     for match in s.results:
#         print(match)
#
# test1()
#
# # create GUI obj for run the code
# def test2():
#     g = Gui()           #gui obj
#     # g.window.Read()   #read the comment pop up on the screen
#     while True:              # gui event(enter, search) values display in screen automatically
#         event, values = g.window.Read()
#         print(event, values)     # values of the event and key term(contains, startswith, endswith)
#
# test2()

# ------------------------------------------
# connect gui to the search engine with loop
def main():
    g = Gui()                    #gui obj
    s = SearchEngine()          # class
    s.load_existing_index()      # load existing index

    while True:
        event, values = g.window.read()   # return values in screen
        # event loop (search, close window, idle, exit)
        if event is None:
            break
        if event == '_INDEX_':
            s.create_new_index(values)

            print()
            print('>> New Index has been Created')
            print()

        if event == 'SPEAK':
            s.speak_now(Values)                 # calling speak_now func()

        if event == '_SEARCH_':
            s.search(values)

            # print results to output element
            print()
            for result in s.results:
                print(result)
            # to print the matching result in the variable using string variable format
            print()
            print('>> There were {:,d} matches out of {:,d} records searched.'.format(s.matches, s.records))
            # print()
            print('>> This query produced the following matches: \n')

if __name__ == '__main__':
    print('Starting program...')
    main()


