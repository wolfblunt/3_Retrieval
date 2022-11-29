import requests
import json


def searchNews_result(searchTerm):
    apiKey = "24920901fc574de0a951c005e96f7036"
    searchURL1 = "https://newsapi.org/v2/everything?q={}&apiKey={}".format(searchTerm, apiKey)
    # searchURL2 = "https://newsapi.org/v2/everything?q={}&page=2&apiKey={}".format(searchTerm, apiKey)
    html_text = requests.get(searchURL1).text
    # html_text2 = requests.get(searchURL2).text

    print(html_text)
    searchQuery = json.loads(html_text)
    # searchQuery2 = json.loads(html_text2)

    searchData = searchQuery["articles"]
    # searchData2 = searchQuery2["articles"]
    l = []
    for i in range(len(searchData)):
        print(searchData[i])
        contentDict = {}
        contentDict["title"] = searchData[i].get("title", "")
        contentDict["url"] = searchData[i].get("url", "")
        contentDict["publishedAt"] = searchData[i].get("publishedAt", "")[:10]
        contentDict["publisher"] = searchData[i]["source"].get("name", "")
        contentDict["urlToImage"] = searchData[i].get("urlToImage", "")
        contentDict["author"] = searchData[i].get("author", "")
        contentDict["description"] = searchData[i].get("description", "")
        print(contentDict)
        l.append(contentDict)
        print("---------------------------------------------")

    # for i in range(len(searchData2)):
    #     print(searchData[i])
    #     contentDict = {}
    #     contentDict["title"] = searchData[i].get("title", "")
    #     contentDict["url"] = searchData[i].get("url", "")
    #     contentDict["publishedAt"] = searchData[i].get("publishedAt", "")[:10]
    #     contentDict["publisher"] = searchData[i]["source"].get("name", "")
    #     contentDict["urlToImage"] = searchData[i].get("urlToImage", "")
    #     contentDict["author"] = searchData[i].get("author", "")
    #     contentDict["description"] = searchData[i].get("description", "")
    #     print(contentDict)
    #     l.append(contentDict)
    #     print("---------------------------------------------")

    return l
