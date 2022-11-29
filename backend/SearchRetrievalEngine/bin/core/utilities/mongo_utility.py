import json
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import uuid
from datetime import datetime
from pymongo.errors import DuplicateKeyError as MongoDuplicateKeyError


class MongoUtility():
    def __init__(self, _mongo_host, _mongo_port):
        super().__init__()
        try:
            self.__mongo_OBJ__ = MongoClient(host=_mongo_host, port=_mongo_port)
            print("Mongo connection established")
        except Exception as e:
            print("Error in establishing connection: " + str(e))
            raise Exception(e)

    def insert_one(self, json_data, database_name, collection_name):
        """
        To insert single document in collection
        :param json_data:
        :param database_name:
        :param collection_name:
        :return: id
        """
        try:
            if not json_data.get("id", ""):
                json_data["timestamp"] = str(datetime.utcnow()).split('.')[0]
                json_data["id"] = self.generating_ramdon_id(collection_name)
            mongo_response = self.__mongo_OBJ__[database_name][collection_name].insert_one(json_data)
            print("Inserted document in mongo")
            return mongo_response.inserted_id
        except MongoDuplicateKeyError:
            raise MongoDuplicateKeyError("Found an existing record with the same ID in MongoDB")
        except Exception as e:
            print("Error in inserting document: " + str(e))
            raise Exception(e)

    def insert_many(self, json_data, collection_name, database_name):
        """
        To insert multiple documents in collection
        :param json_data:
        :param collection_name:
        :param database_name:
        :return: response
        """
        try:
            print("Data Befoe Insert : ", json_data)
            mongo_response = self.__mongo_OBJ__[database_name][collection_name].insert_many(json_data)
            print("MONGO RESPONSE : ", mongo_response)
            # json_mongo_response_object = json.loads(json.dumps(mongo_response))
            data = mongo_response.inserted_ids
            print("Inserted documents in mongo : ", data)
            return "Success"
        except Exception as e:
            print("Error in inserting document: " + str(e))
            raise Exception(e)

    def find_json(self, json_data, database_name, collection_name):
        """
        To find single document in collection
        :param json_data:
        :param database_name:
        :param collection_name:
        :return: response object
        """
        try:
            db = self.__mongo_OBJ__[database_name]
            mongo_response = db[collection_name].find(json_data)
            print("Fetched results from mongo")
            return mongo_response
        except Exception as e:
            print("Error in finding document: " + str(e))
            raise Exception(e)

    def find_all(self, database_name, collection_name):
        """
        To find all the documents
        :param database_name:
        :param collection_name:
        :return: response object
        """
        try:
            db = self.__mongo_OBJ__[database_name]
            mongo_response = db[collection_name].find()
            print("find : --> ", mongo_response)
            print("Fetched results from mongo")
            return mongo_response
        except Exception as e:
            print("Error in finding document: " + str(e))
            raise Exception(e)

    def update_one(self, condition, json_data, _database_name, collection_name):
        """
        To update single document
        :param condition:
        :param json_data:
        :param _database_name:
        :param collection_name:
        :return: success
        """
        try:
            database_connection = self.__mongo_OBJ__[_database_name]
            mongo_response = database_connection[collection_name].update_one(condition, {"$set": json_data})
            print("Updated document from mongo")
            return "success"
        except Exception as e:
            print("Error in updating document: " + str(e))
            raise Exception

    def remove(self, json_data, _database_name, collection_name):
        """
        To delete document from collection
        :param json_data:
        :param _database_name:
        :param collection_name:
        :return: success
        """
        try:
            database_connection = self.__mongo_OBJ__[_database_name]
            mongo_response = database_connection[collection_name].remove(json_data)
            print("Deleted document from mongo")
            return "Success"
        except Exception as e:
            print("Error in deleting document: " + str(e))
            raise Exception

    @staticmethod
    def generating_ramdon_id(collection_name):
        """
        Genterate UUID
        :param collection_name:
        :return:
        """
        try:
            cart_id = collection_name + "_" + str(uuid.uuid4().hex)
            return cart_id
        except Exception as e:
            print("Error in deleting document: " + str(e))
            raise Exception
