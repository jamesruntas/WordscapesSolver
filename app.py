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
    lettersAsString = input("what are the letters to solve? (ABCDE)")
    letters = lettersAsString.split()
    print(letters)
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
    for i in letters:
        for j in letters:
            if j != i:
                AllCombinations.append(int(str(i) + str(j)))
    
    
    with open('words_alpha.txt') as file:
        contents = file.read()
        for i in AllCombinations:
            if i in contents:
                print ('word found')
            else:
                print ('word not found')

        
if __name__=="__main__":
    run()