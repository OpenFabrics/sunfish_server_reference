# Copyright IBM Corp. 2023
# This software is available to you under a BSD 3-Clause License. 
# The full license terms are available here: https://github.com/OpenFabrics/sunfish_server_reference/blob/main/LICENSE

from flask import Flask,request
from sunfish.lib.core import Core
from sunfish.lib.exceptions import *
import os
import requests



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


@app.route('/<path:resource>', methods=["PATCH"])
def patch(resource):
    try:
        data = request.json
        resp = sunfish_core.patch_object('/'+resource, data)
        return resp, 200
    except ResourceNotFound as e:
        return e.message, 404


def register():
    import time
    time.sleep(1)

    print("Register the Agent as a new AggregationSource")
    aggregation_source_event = {
        "@odata.type": "#Event.v1_7_0.Event",
        "Id": "1",
        "Name": "AggregationSourceDiscovered",
        "Context": "",
        "Events": [{
            "EventType": "Other",
            "EventId": "4594",
            "Severity": "OK",
            "Message": "A aggregation source of connection method Redfish located at http://localhost:5001 has been discovered.",
            "MessageId": "ResourceEvent.1.0.AggregationSourceDiscovered",
            "MessageArgs": ["Redfish", "http://localhost:5001"],
            "OriginOfCondition": {
                "@odata.id": "/redfish/v1/AggregationService/ConnectionMethods/CXL"
            }
        }
        ]}
    subscription = sunfish_core.get_object("/redfish/v1/EventService/Subscriptions/SunfishServer")
    requests.post(subscription["Destination"], json = aggregation_source_event)

    print("Inform Sunfish that a new Fabric is available")
    time.sleep(2)

    subscription = sunfish_core.get_object("/redfish/v1/EventService/Subscriptions/SunfishServer")
    fabric_created_event = {
        "@odata.type": "#Event.v1_7_0.Event",
        "Id": "2",
        "Name": "Fabric Created",
        "Context": f"{subscription['Context']}",
        "Events": [ {
          "EventType": "Other",
          "EventId": "4595",
          "Severity": "OK",
          "Message": "New Resource Created ",
          "MessageId": "ResourceEvent.1.0.ResourceCreated",
          "MessageArgs": [],
          "OriginOfCondition": {
           "@odata.id": "/redfish/v1/Fabrics/CXL"
          }
        }]
    }
    requests.post(subscription["Destination"], json=fabric_created_event)


if __name__ == '__main__':
    import threading
    thread = threading.Thread(target=register)
    thread.start()
    host = os.getenv('FLASK_HOST', '127.0.0.1')
    port = os.getenv('FLASK_PORT', '5001')
    app.run(host=host, port=int(port))