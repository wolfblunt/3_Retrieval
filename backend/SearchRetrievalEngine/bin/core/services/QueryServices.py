"""
API's
"""
import json
import traceback
from flask import request, Blueprint
from bin.core.application import SearchQuery, ImageQuery, VideoQuery

# Canvas Blueprint
query = Blueprint("Query", __name__)


@query.route("/FetchSearchResults", methods=["GET"])
def search_result_service():
    """
    API Endpoint for search results
    :return:
    """
    if request.method == 'GET':
        print("Inside Search Results")
        try:
            searchQuery = request.args.get("searchQuery", "")
            results = SearchQuery.search_query_handler(searchQuery)
            response = dict()
            response['status'] = "OK"
            response['message'] = results
            return response
        except Exception as e:
            print(str(e))
            message = 'Unable to query search items'
            return message


@query.route("/seeker/fetchQuery", methods=["POST"])
def post_search_query_service():
    """
    API Endpoint for creating project
    :return:
    """
    if request.method == 'POST':
        print("Inside post_search_query_service")
        try:
            input_json = json.loads(request.get_data())
            print("Input JSON Type: ", type(input_json))
            print("Input JSON : " + str(input_json))
            response = SearchQuery.search_request_handler(input_json)
            print(response)
            return response
        except Exception as e:
            print(str(e))
            message = "Unable to add details in the collection"
            return dict(status="ERROR", message=message)


@query.route("/seeker/ImageFetchQuery", methods=["POST"])
def post_imageSearch_service():
    """
    API Endpoint for creating project
    :return:
    """
    if request.method == 'POST':
        print("Inside post_search_query_service")
        try:
            input_json = json.loads(request.get_data())
            print("Input JSON Type: ", type(input_json))
            print("Input JSON : " + str(input_json))
            response = ImageQuery.fetchImage_handler(input_json)
            print("Image search response : ", response)
            return response
        except Exception as e:
            print(str(e))
            message = "Unable to add details in the collection"
            return dict(status="ERROR", message=message)


@query.route("/seeker/VideoFetchQuery", methods=["POST"])
def post_VideoSearch_service():
    """
    API Endpoint for creating project
    :return:
    """
    if request.method == 'POST':
        print("Inside post_search_query_service")
        try:
            input_json = json.loads(request.get_data())
            print("Input JSON Type: ", type(input_json))
            print("Input JSON : " + str(input_json))
            response = VideoQuery.fetchVideo_handler(input_json)
            print("Video search response : ", response)
            return response
        except Exception as e:
            print(str(e))
            message = "Unable to add details in the collection"
            return dict(status="ERROR", message=message)
