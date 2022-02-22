import itertools
from os import system
from sqlite3 import Time
from unittest import case





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
    
    
def run():
    #display()
    letters = input("what are the letters to solve? (ABCDE)")

    print(letters)
    for letter in letters:
        if letter.isnumeric() == True or len(letters) <=3:
            letters.pop(letter)
        if len(letters)<4:
            Time.sleep(1000)
            print("not enough letters")
            system.exit()

    threeLettersInput= input("Three Letter words allowed? (yes,y,no,n)")
    if threeLettersInput=="yes" or threeLettersInput =="y":
        threeLettersAllowed = True
    elif threeLettersInput=="no" or threeLettersInput=="n":
        threeLettersAllowed = False
    else:
        print("not valid input")
        run()

    AllCombinations = []
    print("letters:  " + letters)
    for i in range(len(letters)+1):
        i+=1
        i+=1
        for combination in itertools.combinations(letters, i): #add search here to see if word has no vowels
            AllCombinations.append(convertTuple(combination))
    print (AllCombinations)
    file =  open('words_alpha.txt')
    

    for line in file: 
        for word in line.split():
            for str in AllCombinations:
                if threeLettersAllowed==True:
                    if str==word and len(str)>=3:
                        print (str)
                if threeLettersAllowed==False:
                    if str==word and len(str)>3:
                        print(str)

def convertTuple(tup):
        # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str



if __name__=="__main__":
    run()