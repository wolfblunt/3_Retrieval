import traceback
from flask import Flask
from flask_compress import Compress
from flask_cors import CORS
from bin.common import AppConfigurations
from bin.core.services.QueryServices import query

# creating app
app = Flask(__name__)

# --------------------------------------------- REGISTER BLUEPRINTS ----------------------------------------------------

app.register_blueprint(query)

# ---------------------------------- CORS configurations for Service endpoints -----------------------------------------

CORS(app, resources={
    r"/*": {"origins": "*"}
})
Compress(app)
# ----------------------------------------------------------------------------------------------------------------------
service_port = AppConfigurations.service_port
service_host = AppConfigurations.service_host

if __name__ == '__main__':
    try:
        print(('Starting service @ port ' + str(service_port)))
        # it is also possible to enable the API directly
        app.run(host=str(service_host), port=int(service_port), debug=True, threaded=True, use_reloader=False)
    except Exception as e:
        traceback.print_exc()
