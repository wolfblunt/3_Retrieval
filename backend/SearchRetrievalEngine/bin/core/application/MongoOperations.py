from bin.common.AppConfigurations import mongo_host, mongo_port, db_name, cart_collection
from bin.core.utilities.mongo_utility import MongoUtility
from datetime import date, datetime


class QuerySearch(object):
    def __init__(self):
        self.mongo_client = MongoUtility(_mongo_port=mongo_port, _mongo_host=mongo_host)

    def list_query_result_collection(self):
        try:
            print("Fetching endpoint details from mongo")
            mongo_content = self.mongo_client.find_all(database_name=db_name,
                                                       collection_name=cart_collection)
            response = list()
            for content in mongo_content:
                del content["_id"]
                response.append(content)
            return response
        except Exception as e:
            import traceback
            print("EROR :", traceback.print_exc())
            print("Failure to fetch cart collection --> {}".format(str(e)))
            raise Exception("Error when fetching cart collection!")

    def add_query_result_collection(self, input_json):
        try:
            mongo_content = self.mongo_client.insert_one(json_data=input_json, database_name=db_name,
                                                         collection_name=cart_collection)
            print("mongo_content : ", mongo_content)
            return True
        except Exception as e:
            import traceback
            print("ERROR :", traceback.print_exc())
            print("Failure to fetch cart collection --> {}".format(str(e)))
            raise Exception("Error when fetching cart collection!")

    def add_multiple_search_results_into_collection(self, input_json):
        try:
            print("Type InputJson : ", type(input_json))
            flag = False
            for data in input_json:
                print("data : ", data)
                flag = True
                if not data.get("id", ""):
                    data["timestamp"] = str(datetime.utcnow()).split('.')[0]
                    data["id"] = self.mongo_client.generating_ramdon_id(cart_collection)
            print("INPUT JSON MULTI : ", input_json)
            if flag:
                mongo_content = self.mongo_client.insert_many(json_data=input_json, database_name=db_name,
                                                              collection_name=cart_collection)
                return True
            else:
                return False

        except Exception as e:
            import traceback
            print("ERROR :", traceback.print_exc())
            print("Failure to fetch cart collection --> {}".format(str(e)))
            raise Exception("Error when fetching cart collection!")
