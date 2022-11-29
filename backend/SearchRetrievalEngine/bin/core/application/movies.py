import requests
import json
from rotten_tomatoes_client import RottenTomatoesClient
from operator import itemgetter


def searchMovie_result(searchTerm):
    try:
        searchData = RottenTomatoesClient.search(term=searchTerm, limit=100)
        print("Rotten : ")
        print(searchData)
        l = []
        movieslist = searchData.get("movies", [])
        print("movieslist: ", movieslist)
        if movieslist:
            for i in range(len(movieslist)):
                print(movieslist[i])
                contentDict = {}
                contentDict["title"] = movieslist[i].get("name", "")
                contentDict["url"] = "https://www.rottentomatoes.com" + movieslist[i].get("url", "")
                contentDict["year"] = movieslist[i].get("year", "")
                contentDict["type"] = "Movie"
                contentDict["imageURL"] = movieslist[i].get("image", "")
                rate = movieslist[i].get("meterScore", "")
                if rate is not "" :
                    contentDict["rating"] = float(rate)
                else :
                    contentDict["rating"] = 0
                starCast = movieslist[i].get("castItems", [])
                if starCast:
                    for i in range(len(starCast) - 1):
                        contentDict["starCast"] = starCast[i].get("name", "") + ","

                    if contentDict.get("starCast", ""):
                        contentDict["starCast"] += starCast[-1].get("name", "")
                    else:
                        contentDict["starCast"] = ""
                else:
                    contentDict["starCast"] = ""
                print(contentDict)
                l.append(contentDict)
                print("---------------------------------------------")
        print("l : ", l)
        tvSeries = searchData.get("tvSeries", [])
        counter = 0
        totalCount = len(tvSeries)
        if tvSeries:
            for i in range(totalCount):
                print(tvSeries[i])
                contentDict = {}
                contentDict["title"] = tvSeries[i].get("title", "")
                contentDict["url"] = "https://www.rottentomatoes.com" + tvSeries[i].get("url", "")
                contentDict["year"] = tvSeries[i].get("startYear", "")
                contentDict["type"] = "TV-Series"
                contentDict["imageURL"] = tvSeries[i].get("image", "")
                rate = tvSeries[i].get("meterScore", "")
                if rate is not "" :
                    contentDict["rating"] = float(rate)
                else :
                    contentDict["rating"] = 0
                contentDict["index"] = (totalCount - counter) / totalCount
                contentDict["starCast"] = ""
                print(contentDict)
                l.append(contentDict)
                print("---------------------------------------------")

        return l
    except Exception as e:
        print(e)


def rank_algorithm_movies(movies_list, query):
    words = query.split(' ')
    movie_count = 0
    tv_series_count = 0
    length = len(movies_list)
    for movie in movies_list:
        rating_score = 0
        if movie['rating'] is not None:
            rating_score = (movie['rating'] * 3) / 100

        placement_score = 0
        if movie['type'] == "Movie":
            placement_score = ((length - movie_count) / length) * 30
            movie_count = movie_count + 1
        elif movie['type'] == "TV-Series":
            placement_score = ((length - tv_series_count) / length) * 20
            tv_series_count = tv_series_count + 1

        name_score = 0
        if movie['title'] is not None:
            occur = 0
            for word in words:
                if word.lower() in movie['title'].lower():
                    occur = occur + 1
            name_score = (occur / len(words)) * 30

        recent_year_score = 0
        if movie['year'] is not None:
            recent_year_score = ((movie['year'] - 1950) / 72) * 10

        total_score = recent_year_score + name_score + placement_score + rating_score
        movie['Score'] = total_score

    ranked_product_details = sorted(movies_list, key=itemgetter('Score'), reverse=True)

    return ranked_product_details
