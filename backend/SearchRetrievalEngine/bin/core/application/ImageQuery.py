from serpapi import GoogleSearch


def fetchImage_handler(input_json):
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
                "q": "{}".format(searchQuery),
                "tbm": "isch",
                "ijn": "0",
                "api_key": "4d47a3b0384d54ff78cac9b93a1dc71ac8a696c73c708a9892f8fbff53cc6148"
            }

            search = GoogleSearch(params)
            results = search.get_dict()
            response["message"] = results["images_results"]
            response["status"] = "OK"

        else:
            response["message"] = "Invalid Query"
            response["status"] = "ERROR"

        return response

    except Exception as e:
        print(e)
