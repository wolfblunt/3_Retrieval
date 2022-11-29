import requests
import json
from operator import itemgetter


def searchDOAJ_result(searchTerm):
    searchURL = "https://doaj.org/api/search/articles/title:{term}?pageSize=50&page=1".format(term=searchTerm)
    # html_text = requests.get('https://doaj.org/api/search/articles/title:python?pageSize=20&page=1').text
    html_text = requests.get(searchURL).text

    print(html_text)
    searchQuery = json.loads(html_text)

    searchData = searchQuery["results"]
    l = []
    counter = 1
    totalCount = len(searchData)
    for i in range(totalCount):
        print(searchData[i]["bibjson"])
        contentDict = {}
        contentDict["title"] = searchData[i]["bibjson"].get("title", "")
        contentDict["url"] = searchData[i]["bibjson"]["link"][0]["url"]
        contentDict["year"] = int(searchData[i]["bibjson"].get("year", 0))
        contentDict["publisher"] = searchData[i]["bibjson"].get("journal", {}).get("publisher", "")
        author = searchData[i]["bibjson"].get("author", [])
        contentDict["index"] = (totalCount - counter) / totalCount
        contentDict["Source"] = "DOAJ"
        if author:
            contentDict["author"] = author[0].get("name", "")
        print(contentDict)
        l.append(contentDict)
        counter += 1
        print("---------------------------------------------")

    return l


def rank_algorithm_articles(articles_list, query):
    words = query.split(' ')
    for article in articles_list:
        placement_score = article['index'] * 20

        name_score = 0
        if article['title'] is not None:
            occur = 0
            for word in words:
                if word.lower() in article['title'].lower():
                    occur = occur + 1
            name_score = (occur / len(words)) * 35

        recent_year_score = 0
        if article['year'] != None:
            recent_year_score = (int((article['year']) - 1900) / 122) * 45

        total_score = recent_year_score + name_score + placement_score
        article['Score'] = total_score

    ranked_product_details = sorted(articles_list, key=itemgetter('Score'), reverse=True)

    return ranked_product_details
