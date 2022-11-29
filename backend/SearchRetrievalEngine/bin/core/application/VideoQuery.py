from serpapi import GoogleSearch


def fetchVideo_handler(input_json):
    """
    This method is for fetching image json data for an input query
    :param input_json:
    :return:
    """
    try:
        searchQuery = input_json.get("searchTerm", "")
        response = dict()
        if searchQuery:
            params = {
                "engine": "youtube",
                "search_query": "{}".format(searchQuery),
                "api_key": "4d47a3b0384d54ff78cac9b93a1dc71ac8a696c73c708a9892f8fbff53cc6148"
            }

            search = GoogleSearch(params)
            results = search.get_dict()
            print("results: ", results)
            topNews = results.get("top_news", [])
            videoResults = results.get("video_results", [])
            resultlist = topNews + videoResults
            response["message"] = resultlist
            response["status"] = "OK"

        else:
            response["message"] = "Invalid Query"
            response["status"] = "ERROR"

        return response

    except Exception as e:
        print(e)
