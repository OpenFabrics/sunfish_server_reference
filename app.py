# Copyright IBM Corp. 2023
# This software is available to you under a BSD 3-Clause License. 
# The full license terms are available here: https://github.com/OpenFabrics/sunfish_server_reference/blob/main/LICENSE
import os
import traceback

from flask import Flask, request, render_template
from sunfish.lib.core import Core
from sunfish.lib.exceptions import *
import logging

FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT, level=logging.DEBUG)

logger = logging.getLogger("Server")

conf = {
    "storage_backend": "FS",
	"redfish_root": "/redfish/v1/",
	"backend_conf" : {
		"fs_root": "Resources",
		"subscribers_root": "EventService/Subscriptions"
	},
	"handlers": {
		"subscription_handler": "redfish",
		"event_handler": "redfish"

	}
}

# initialize flask

template_dir = os.path.abspath('./templates_web')
app = Flask(__name__, template_folder=template_dir)
sunfish_core = Core(conf)

@app.route('/browse')
def browse():
    return render_template('browse.html')

# Usa codici http
@app.route('/<path:resource>', methods=["GET"], strict_slashes=False)
def get(resource):
	logger.debug(f"GET on: {request.path}")
	try:
		resp = sunfish_core.get_object(request.path)

		return resp, 200
	except ResourceNotFound as e:
		return e.message, 404

@app.route('/<path:resource>', methods=["POST"], strict_slashes=False)
def post(resource):
	logger.debug("POST")
	try :
		if resource == "EventListener":
			resp = sunfish_core.handle_event(request.json)
		else:
			resp = sunfish_core.create_object(request.path, request.json)

		return resp
	except CollectionNotSupported as e:
		return e.message, 405 # method not allowed
	except AlreadyExists as e:
		return e.message, 409 # Conflict
	except PropertyNotFound as e:
		return e.message, 400

@app.route('/<path:resource>', methods=["PUT"], strict_slashes=False)
def put(resource):
	try:
		data = request.json
		resp = sunfish_core.replace_object(data)
		return resp, 200
	except ResourceNotFound as e:
		return e.message, 404

@app.route('/<path:resource>', methods=["PATCH"], strict_slashes=False)
def patch(resource):
	try:
		logger.debug("PATCH")
		data = request.json
		resp = sunfish_core.patch_object(path=request.path, payload=data)
		return resp, 200
	except ResourceNotFound as e:
		return e.message, 404
	except Exception:
		traceback.print_exc()

@app.route('/<path:resource>', methods=["DELETE"], strict_slashes=False)
def delete(resource):
	try:
		resp = sunfish_core.delete_object(request.path)
		return resp, 200
	except ResourceNotFound as e:
		return e.message, 404
	except ActionNotAllowed as e:
		return e.message, 403 # forbidden
	except InvalidPath as e:
		return e.message, 400

# we run app debugging mode
app.run(debug=False)