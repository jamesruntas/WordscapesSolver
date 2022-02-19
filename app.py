import requests






def query_dictionary(key, word):
    query = requests.get('https://dictionaryapi.com/api/v3/references/collegiate/json/' + word + '?key=' + key)
    response = query.json()
    try:
        returnDict = 1
    except:
        returnDict = null
        
    print (word)
    print (response)
    return response
    

    
if __name__=="__main__":
    key = "8fcad4b1-127e-4634-b97a-b20de7b0ed80"
    query_dictionary(key, "apple")
    	
    	
    	
    	
    	
    	
    	


if __name__=="__main__":
    main()