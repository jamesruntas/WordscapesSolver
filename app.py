import requests


APIKEY = "8fcad4b1-127e-4634-b97a-b20de7b0ed80"
dictionary = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/"
suffix = "?key=8fcad4b1-127e-4634-b97a-b20de7b0ed80"



def main():
    word = "Apple"
    query = word+suffix

    response = requests.request("GET", dictionary, headers=query)
    print(response.text)
    



if __name__=="__main__":
    main()