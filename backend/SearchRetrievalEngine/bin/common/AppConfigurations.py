"""
    Configuration variables
"""

import configparser
import __root__

# Root path
root_path = __root__.path()

# Properties file
CONFIGURATION_FILE = "application_conf/settings.conf"

ENV_CONF_FILE = "conf/settings.conf"

# Config file parser
parser = configparser.RawConfigParser(allow_no_value=True)

parser.read([CONFIGURATION_FILE, ENV_CONF_FILE])

# Service host
service_host = parser.get("SERVICE", "service_host")

# Service port number
service_port = int(parser.get("SERVICE", "service_port"))

mongo_uri = parser.get("MONGO", "mongo_uri")
mongo_username = parser.get("MONGO", "mongo_username")
mongo_password = parser.get("MONGO", "mongo_password")
mongo_port = int(parser.get("MONGO", "mongo_port"))
mongo_host = parser.get("MONGO", "mongo_host")

db_name = parser.get('MONGO', 'application_db')


# Mongo collections
cart_collection = parser.get('MONGO', 'cart_collection')

