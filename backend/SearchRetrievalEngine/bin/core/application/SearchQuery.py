"""
Search Layer
"""
from bin.core.application.doajSearch import searchDOAJ_result, rank_algorithm_articles
from bin.core.application.oreillySearch import searchOreilly_result
from bin.core.application.flipkart import get_products_by_name_flipkart, rank_algorithm_ecommerce
from bin.core.application.amazon import get_products_by_name_amazon
from bin.core.application.newsSearch import searchNews_result
from bin.core.application.movies import searchMovie_result, rank_algorithm_movies
from bin.core.application import ImageQuery, VideoQuery


from bin.core.application.MongoOperations import QuerySearch


def search_query_handler(searchQuery):
    """
    This method is for fetching cart items
    :return: User ID JSON
    """
    try:
        response = dict()
        if searchQuery:
            l = []
            l.append(searchDOAJ_result(searchQuery))
            l.append(searchOreilly_result(searchQuery))
            response["message"] = l
            response["status"] = "OK"
        else:
            response["message"] = "Invalid Query"
            response["status"] = "ERROR"
        return response
    except Exception as e:
        import traceback
        print("ERROR :", traceback.print_exc())
        print(str(e))
        raise Exception(str(e))


def search_request_handler(input_json):
    """
    This method is for searching item into cart
    :param input_json:
    :return:
    """
    try:
        response = dict()
        print(input_json)
        searchType = input_json["searchType"]
        searchDomain = input_json.get("searchDomain", "")
        searchQuery = input_json.get("searchTerm", "")
        l = []
        if searchType == "text":
            if searchDomain == "eCommerce":
                l2 = get_products_by_name_amazon(searchQuery)
                # print("l2 : ", l2)
                l1 = get_products_by_name_flipkart(searchQuery)
                # print("l1 : ", l1)
                if l1 is not None:
                    l = l1
                if l2 is not None:
                    l += l2
                l = rank_algorithm_ecommerce(l, searchQuery)
            if searchDomain == "article":
                l1 = searchDOAJ_result(searchQuery)
                l2 = searchOreilly_result(searchQuery)
                l = l1 + l2
                l = rank_algorithm_articles(l, searchQuery)

            if searchDomain == "news":
                l = searchNews_result(searchQuery)

            if searchDomain == "movie":
                l = searchMovie_result(searchQuery)
                l = rank_algorithm_movies(l, searchQuery)
            
        if l:
            response["message"] = l
            response["status"] = "OK"
        else:
            response["message"] = "Invalid query to perform this action"
            response["status"] = "ERROR"
        print("Final Response : ", response)
        return response
    except Exception as e:
        import traceback
        print("ERROR :", traceback.print_exc())
        print(str(e))
        raise Exception(str(e))
