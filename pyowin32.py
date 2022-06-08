import requests    
 
def NewsFromTOI():
     
    # BBC news api
    # following query parameters are used
    # source, sortBy and apiKey
    query_params = {
      "source": "toi-news",
      "sortBy": "entertainment",
      "apiKey": "d78c5201a1524530a76490e5dac995ba"
    }
    main_url = "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=d78c5201a1524530a76490e5dac995ba"
 
    # fetching data in json format
    r = requests.get(main_url, params=query_params)
    open_toi_page = r.json()
 
    # getting all articles in a string article
    article = open_toi_page["articles"]
 
    # empty list which will
    # contain all trending news
    results = []
     
    for ar in article:
        results.append(ar["title"])
         
    for i in range(len(results)):
         
        # printing all trending news
        print(i + 1, results[i])
 
    #to read the news out loud for us
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(results)                
 
# Driver Code
if __name__ == '__main__':
     
    # function call
    NewsFromTOI()
