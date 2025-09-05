# Copyright Hewlett Packard Enterprise Development LP 2024
# This software is available to you under a BSD 3-Clause License. 
# The full license terms are available here: https://github.com/OpenFabrics/sunfish_server_reference/blob/main/LICENSE
import os
import traceback
import json

import logging
import requests

FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logger = logging.getLogger("strip_manager")

'''
"Oem": {
        "Sunfish_RM": {
            "@odata.type": "#SunfishExtensions.v1_0_0.ResourceExtensions",
            "ManagingAgent": {
                "@odata.id": "/redfish/v1/AggregationService/AggregationSources/9a2d39cb-26af-4fb3-aa36-8fa5abc9430d"
            },
            BoundaryComponent": "unknown"
        }
    }
'''


init_Sunfish_RM = {
        "@odata.type": "#SunfishExtensions.v1_0_0.ResourceExtensions",
        "BoundaryComponent": "owned"
    }
    #  BoundaryComponent:  ["owned", "foreign", "boundaryPort", "unknown"]

def fix_missing_Id(path: str):
    try:
        try:
            if os.path.exists(path):
                # Read json from file.
                with open(path, 'r') as data_json:
                    
                    logger.debug(f"reading file {path}")
                    redfish_obj = json.load(data_json)
                    data_json.close()

                # Update the keys of payload in json file.
                if "Id" not in redfish_obj:
                    Id = redfish_obj["@odata.id"].split("/")[-1]
                    logger.info(f"""object {redfish_obj["@odata.id"]} missing an Id property """)
                    redfish_obj["Id"] = Id
                    print(json.dumps(redfish_obj, indent=4))
                    #with open(path, 'w') as f:
                    #    json.dump(redfish_obj, f, indent=4, sort_keys=True)
                    #    f.close()
            else:
                logger.info(f"""file {path} not found  """)
            # Write the updated json to file.

        except:
            logger.debug("Something wrong with fix_missing_Id function")
            logger.info(f"skipping file {path}")
            pass
    except:
        pass


def clear_managing_agent(path: str):
    try:
        try:
            if os.path.exists(path):
                # Read json from file.
                with open(path, 'r') as data_json:
                    
                    logger.debug(f"reading file {path}")
                    redfish_obj = json.load(data_json)
                    data_json.close()

                # Update the keys of payload in json file.
                if "Oem" not in redfish_obj:
                    redfish_obj["Oem"] = {"Sunfish_RM": init_Sunfish_RM}
                elif "Sunfish_RM" not in redfish_obj["Oem"]:
                    redfish_obj["Oem"]["Sunfish_RM"] = init_Sunfish_RM
                else:
                    if "ManagingAgent" in redfish_obj["Oem"]["Sunfish_RM"]:
                        # We need to strip it 
                        removed_value = redfish_obj["Oem"]["Sunfish_RM"]["ManagingAgent"].pop("@odata.id", None)
                        logger.info(f"""Stripping the object {redfish_obj["@odata.id"]} of managing agent {removed_value}""")
                        removed_value = redfish_obj["Oem"]["Sunfish_RM"].pop("ManagingAgent", None)
                       
                    if "BoundaryComponent" not in redfish_obj["Oem"]["Sunfish_RM"]:
                                redfish_obj["Oem"]["Sunfish_RM"]["BoundaryComponent"] = init_Sunfish_RM["BoundaryComponent"]

                with open(path, 'w') as f:
                    json.dump(redfish_obj, f, indent=4, sort_keys=True)
                    f.close()
            else:
                logger.info(f"""file {path} not found  """)
            # Write the updated json to file.

        except:
            logger.debug("Something wrong with stripping function")
            logger.info(f"skipping file {path}")
            pass
    except:
        pass


def bulk_mod_json(path: str):
    try: 
        if os.path.exists(path):
        # Read list of json files from path.
            with open(path, 'r') as data_file: 
                logger.debug(f"reading file {path}")
                list_of_files = data_file.readlines()
                data_file.close()
            for line in list_of_files:
                working_on=line.strip()
                print(f"processing {working_on}")
                clear_managing_agent(working_on)
                fix_missing_Id(working_on)
        else:
            print(f"couldn't find file {path}")

    except:
        pass
