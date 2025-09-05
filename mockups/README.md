# mockups
This repository is for merging different  mockups for different Sunfish_Service and Sunfish_Agent instances of the sunfish_server_reference application.
All mockups herein are derivatives of the OFMFWG/mockups repo on github.
The OFMFWG/mockups will be archived, and all future development of mockups for the Sunfish_server_reference configurations will be checked into this sunfish_server_reference/mockups directory.
All mockups herein are a point-in-time view of OFMF potential configurations.
Currently there are these two configurations of a Sunfish_Service and Sunfish_Agents topology:
- A CXL mockup topology based on 3 instances of the sunfish_server_reference:  Dual CXL Sunfish_Agents whose inventories are aggregated into one CXL fabric by the Sunfish_Service instance.
- An NVMeoF mockup topology based on 2 instances of the sunfish_server_reference application:   A single NVMeoF_Agent instance which uploads it NVMeoF resources to the single Sunfish_Service application.

This directory contains the following mockup sets in their respective directories:
- nvmeof-mockups:  a set of Redfish NVMe resources describing NVMeoF endpoints:  to be used as the NVMeoF_Agent initial resources to be uploaded to a Sunfish_Service.
- server_start_Resources: a basic set of the initial resources needed to instantiate and run a simple Sunfish_Service which would then aggregate resources from one or more Sunfish_Agent instances.
- fm_agent_Resources:  a set of Redfish CXL resources describing a CXL fabric containing one fabric switch, a few systems, and associated chassis and endpoints:  to be used as the fabric manager agent's initial resources to be uploaded to the Sunfish_Service.
- am_agent_Resources:  a set of Redfish CXL resources describing a CXL fabric containing one appliance switch, a few CXL memory devices, and associated chassis and endpoints:  to be used as the appliance manager agent's initial resources to be uploaded to the Sunfish_Service.
- utils_Resources:  a set of aggregated CXL resources describing a CXL fabric containing one fabric switch, some number of systems, a CXL appliance switch with attached CXL memory devices, plus the associated chassis and endpoint objects: to be used as an initial set of CXL resources to a single instance of a Sunfish_Service application.  This configuration requires no Sunfish_Agent instance, and will not run properly should a CXL Sunfish_Agent instance be present.
- sc24-PoC: a copy of the Redfish CXL resources used in the CXL dual CXL Agent and single Sunfish_Services demos which were shown at Supercompute '24.  These mockups are very similar those CXL resources listed above, but these are no longer being maintained, and they may not be compatible with subsequent revisions to the sunfish_server_reference application code or the sunfish_library_reference code.  They are included herein so that the OFMFWG/mockups repository on Github can be archived. 



