from unittest import case
import requests
import tkinter
import itertools





def query_dictionary(word):
    apikey = "8fcad4b1-127e-4634-b97a-b20de7b0ed80" #comment this out
    try:
        query = requests.get('https://dictionaryapi.com/api/v3/references/collegiate/json/' + word + '?key=' + apikey)
        response = query.json()
        if response.wordValue != null:
            return True
        else:
            return False
    except:
        print("Dictionary Error: Likely issues - Internet Connection, Bad API Key, Merriam Webster is unresponsive")
        SystemError
    

def display():
    m = tkinter.Tk()
    m.mainloop()


    
def run():
    display()
    lettersAsString = input("what are the letters to solve? (ABCDE)")
    letters = lettersAsString.split()
    
    for letter in letters:
        if letter.isalpha != True or len(letters) <=3:
            print("not valid input")
            run()


    threeLettersInput= input("Three Letter words allowed? (yes,y,no,n)")
    if threeLettersInput=="yes" or threeLettersInput =="y":
        threeLettersAllowed = True
    elif threeLettersInput=="no" or threeLettersInput=="n":
        threeLettersAllowed = False
    else:
        print("not valid input")
        run()

    AllCombinations = []
    for i in range(len(letters)):
        AllCombinations += list(itertools.combinations(letters, i))

    
    





    query_dictionary(word)








if __name__=="__main__":
    run()

    	
    	
    	
    	
    	
    	
    	


if __name__=="__main__":
    main()