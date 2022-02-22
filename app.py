import itertools
from os import system
from sqlite3 import Time
import tkinter
from unittest import case
from tkinter import * 


global threeLettersFlag
global madeWords
global gui
global label
madeWords= []
gui = tkinter.Tk()
label = Label(gui, text = "")


#def query_dictionary_API(word):
    #apikey = "" #put your key here
    #try:
        #query = requests.get('https://dictionaryapi.com/api/v3/references/collegiate/json/' + word + '?key=' + apikey)
       # response = query.json()
       # if response.wordValue != null:
      #      return True
      #  else:
      #      return False
   # except:
    #    print("Dictionary Error: Likely issues - Internet Connection, Bad API Key, Merriam Webster is unresponsive")
    #    return 

def display():

    gui.configure(background="light grey")
    gui.title("Wordscapes Solver")
    gui.geometry("350x500")
    inputLetters = StringVar()
    threeLettersFlag = False

    expression_field = Entry(gui, textvariable=inputLetters)
    solveButton = Button(gui, text=' Solve ', fg='black', bg='light blue',
				command=lambda: run(inputLetters.get(),threeLettersFlag), height=1, width=7)
    threeLettersButtonOff = Button(gui, text=' Three Letters not allowed ', fg='black', bg='red',
				command=lambda: threeLetters(False), height=1, width=18)
    threeLettersButtonOn = Button(gui, text=' Three Letters allowed ', fg='black', bg='green',
				command=lambda: threeLetters(True), height=1, width=15)

    expression_field.pack()
    threeLettersButtonOff.pack()
    threeLettersButtonOn.pack()
    solveButton.pack()
    

    gui.mainloop()



def run(letters,threelettersFlag):
    for letter in letters:
        if letter.isnumeric() == True or len(letters) <=3:
            letters.pop(letter)

    AllCombinations = []
    print("letters:  " + letters)
    for i in range(len(letters)+1):
        i+=1
        i+=1
        for combination in itertools.combinations(letters, i): #add search here to see if word has no vowels
            AllCombinations.append(convertTuple(combination))
    print ("all letter combos")
    print (AllCombinations)
    file =  open('words_alpha.txt')
    
    madeWords = []
    for line in file: 
        for word in line.split():
            for str in AllCombinations:
                if threelettersFlag==True:
                    if str==word and len(str)>=3:
                        madeWords.append(str)
                if threelettersFlag==False:
                    if str==word and len(str)>3:
                        madeWords.append(str)
    print ("words made:")
    print (madeWords)
    label = Label(gui, text = madeWords)
        
    label.pack()
    return madeWords

def convertTuple(tup):
    # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str

def threeLetters(flag):
    threeLettersFlag = flag

if __name__ == "__main__":
    display()    