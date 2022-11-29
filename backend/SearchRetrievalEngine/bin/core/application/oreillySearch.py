import requests
import json


def searchOreilly_result(searchTerm):
    searchURL = "https://learning.oreilly.com/api/v2/search/?query={term}".format(term=searchTerm)
    # html_text = requests.get('https://learning.oreilly.com/api/v2/search/?query=python').text

    html_text = requests.get(searchURL).text

    print(html_text)
    searchQuery = json.loads(html_text)

    searchData = searchQuery["results"]
    l = []
    counter = 0
    totalCount = len(searchData)
    for i in range(totalCount):
        # print(searchData[i])
        contentDict = {}
        contentDict["url"] = "https://learning.oreilly.com/library/view/book/" + searchData[i]["archive_id"] + "/"
        contentDict["title"] = searchData[i].get("title", "")
        contentDict["publisher"] = searchData[i].get("publishers", [])[0]
        yearr = searchData[i].get("issued", "")[:4]
        if yearr is not "":
            contentDict["year"] = int(yearr)
        else:
            contentDict["year"] = 0
        contentDict["author"] = searchData[i].get("authors", [])[0]
        contentDict["Source"] = "Oreilly"
        contentDict["index"] = (totalCount - counter) / totalCount
        print(contentDict)
        l.append(contentDict)
        counter += 1
        print("---------------------------------------------")

    return l
