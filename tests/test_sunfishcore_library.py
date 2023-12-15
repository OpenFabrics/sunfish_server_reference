# Copyright IBM Corp. 2023
# This software is available to you under a BSD 3-Clause License. 
# The full license terms are available here: https://github.com/OpenFabrics/sunfish_library_reference/blob/main/LICENSE

from http.server import HTTPServer
import json
import os
from sunfishcorelib.sunfishcorelib.exceptions import *
from sunfishcorelib.sunfishcorelib.core import Core
import pytest
import test_utils
import tests_template
from werkzeug.wrappers import Request
from werkzeug.wrappers import Response
from pytest_httpserver import HTTPServer
import requests

DESTINATION_HOST = "https://mock-destination.com"

class TestSunfishcoreLibrary():

    @classmethod
    def setup_class(cls):
        cls.conf = {
            "storage_backend": "FS",
	        "redfish_root": "/redfish/v1/",
	        "backend_conf" : {
		        "fs_root": "Resources"
	        }
        }
        cls.core = Core(cls.conf)
        http_server = HTTPServer('127.0.0.1', 8000)
        cls.setup_server(cls, http_server)

    #TEST EVENT
    def setup_server(cls, http_server: HTTPServer):
        http_server.expect_request("/127.0.0.1:8000").respond_with_data('OK')
        cls.core.handle_event(tests_template.test_event1)
        resp = requests.get(http_server.url_for("127.0.0.1:8000"))
        assert resp.text == 'OK'
        
    
    def test_event(self):
        print('test event')


    #   TEST DELETE
    # def test_delete_object(self):
    #     ids = os.listdir(os.path.join(self.conf["redfish_root"], 'Fabrics', 'CXL', 'Zones'))
    #     print(ids)
        # system_url = os.path.join(self.conf["redfish_root"], 'Fabrics', 'CXL', 'Zones', '1')
        # self.core.delete_object(system_url)
        # assert test_utils.check_delete(system_url) == True

    # def test_delete_object2(self):
    #     system_url = os.path.join(self.conf["redfish_root"], 'Fabrics', 'CXL', 'Switches', 'CXL', 'Ports', 'D1')
    #     self.core.delete_object(system_url)
    #     assert test_utils.check_delete(system_url) == True

    # def test_delete_exception(self):
    #     system_url = os.path.join(self.conf["redfish_root"], 'Fabrics', 'CXL', 'Zones', '1')
    #     with pytest.raises(ResourceNotFound):
    #         self.core.delete_object(system_url)

    # # TEST POST
    # def test_post_object(self):
    #     self.core.create_object(tests_template.test_post_zones_1)
    #     assert test_utils.check_object(tests_template.test_post_zones_1, self.conf["redfish_root"]) == True
   
    # def test_post_object2(self):
    #     self.core.create_object(tests_template.test_post_ports)
    #     assert test_utils.check_object(tests_template.test_post_ports, self.conf["redfish_root"]) == True

    # def test__collection_exception(self):
    #     with pytest.raises(CollectionNotSupported):
    #         self.core.create_object(tests_template.test_collection)
    
    # def test_post_exception(self):
    #     with pytest.raises(AlreadyExists):
    #         self.core.create_object(tests_template.test_post_zones_1)
    
    # # TEST GET
    # def test_get(self):
    #     system_url = os.path.join(self.conf["redfish_root"], 'Fabrics', 'CXL', 'Zones', '1')
    #     assert self.core.get_object(system_url) == tests_template.test_post_zones_1

    # def test_get2(self):
    #     system_url = os.path.join(self.conf["redfish_root"], 'Fabrics', 'CXL', 'Switches', 'CXL', 'Ports', 'D1')
    #     assert self.core.get_object(system_url) == tests_template.test_post_ports

    # def test_get_exception(self):
    #     system_url = os.path.join(self.conf["redfish_root"], 'Systems', '-1')
    #     with pytest.raises(ResourceNotFound):
    #         self.core.get_object(system_url)

    # # TEST PUT
    # def test_put(self):
    #     payload = tests_template.test_put
    #     assert self.core.replace_object(payload) == tests_template.test_put["@odata.id"]
    #     #assert test_utils.check_update(payload, self.conf["redfish_root"]) == True

    # def test_put_exception(self):
    #     payload = tests_template.test_update_exception
    #     with pytest.raises(ResourceNotFound):
    #         self.core.replace_object(payload)

    # # TEST PATCH
    # def test_patch(self):
    #     assert self.core.patch_object(tests_template.test_patch) == "/redfish/v1/Fabrics/CXL/Zones/1"

    # def test_patch_exception(self):
    #     payload = tests_template.test_update_exception
    #     with pytest.raises(ResourceNotFound):
    #         self.core.patch_object(payload)

    # # TEST SUBSCRIPTION
    # def test_subscriptions(self):
    #     assert self.core.create_object(tests_template.test_sub1) 

## CAMBIARE I TEST - ora gli id vengono auto generati