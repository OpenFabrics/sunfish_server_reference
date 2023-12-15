# Copyright IBM Corp. 2023
# This software is available to you under a BSD 3-Clause License. 
# The full license terms are available here: https://github.com/OpenFabrics/sunfish_server_reference/blob/main/LICENSE

from flask import Flask
from sunfishcorelib.sunfishcorelib.core import Core
from sunfishcorelib.sunfishcorelib.exceptions import *
import os

conf = {
    "storage_backend": "FS",
    "redfish_root": "/redfish/v1/",
    "backend_conf" : {
        "fs_root": "CXLAgent",
        "subscribers_root": "EventService/Subscriptions"
    },
    "handlers": {
        "subscription_handler": "redfish",
        "event_handler": "redfish"
    }
}

app = Flask(__name__)
sunfish_core = Core(conf)

@app.route('/<path:resource>', methods=["GET"])
def get(resource):
	try:
		resp = sunfish_core.get_object('/'+resource)
		return resp, 200
	except ResourceNotFound as e:
		return e.message, 404

if __name__ == '__main__':
    host = os.getenv('FLASK_HOST', '127.0.0.1')
    port = os.getenv('FLASK_PORT', '5001')
    app.run(host=host, port=int(port))