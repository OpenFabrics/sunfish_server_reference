#! /bin/bash
set -e
# reset the Sunfish Server resources
echo  "curl -X POST -H "Content-Type: application/json" localhost:5000/ResetResources"
 curl -X POST -H "Content-Type: application/json" localhost:5000/ResetResources

# reset the sideloader Agent Server (the FM agent) resources
 echo  "curl -X POST -H "Content-Type: application/json" localhost:5001/ResetResources"
 curl -X POST -H "Content-Type: application/json" localhost:5001/ResetResources

echo "register sideloader (proxy for RealHW) agent"
curl -X POST -H "Content-Type: application/json" -d@register_RealHW_API.json localhost:5000/EventListener

echo "retrieve RealHW API UUID assigned to sideloader agent"
curl -X GET -H "Content-Type: application/json"  localhost:5001/redfish/v1/EventService/Subscriptions/SunfishServer | jq | tee ./temp_RealHW_Subscriber.json

echo "extract sideloader UUID"
RealHW_UUID=$(jq -r '.Context' temp_RealHW_Subscriber.json)
echo $RealHW_UUID

echo "find AggregationSource $RealHW_UUID in Sunfish Resources"
ag_src_file="../../sc24_sunfish_server/Resources/AggregationService/AggregationSources/$RealHW_UUID/index.json"
echo $ag_src_file

# replace following URL with real hardware host URL:  127.0.0.1:5001 is for a local Sunfish Agent emulator
RealHW_host_URL='http://127.0.0.1:5001'
echo $RealHW_host_URL
sideloader_hostname=$(jq -r '.HostName' $ag_src_file)
echo $sideloader_hostname

# Update the HostName value using sed (in place)
sed -i "s|$sideloader_hostname|$RealHW_host_URL|" $ag_src_file 

# File containing the proper upload event format
upload_template="upload_RealHW_API.json"

# Key and new value
new_value=$RealHW_UUID
echo $new_value
# Update the value using sed
# note: the following updates all UUID-formated values, had better be only one!
sed  "s/........-....-....-....-............/$new_value/" $upload_template > temp_upload_template.json
cat temp_upload_template.json
# temp_upload_template.json file now contains the correct UUID to use in the 'resource created' event.
echo "trigger upload of RealHW inventory via an event from sideloader Agent "
curl -X POST -H "Content-Type: application/json" -d@temp_upload_template.json localhost:5000/EventListener
# just a final read of the Sunfish Fabrics collection to validate there is now a CXL Fabric 
echo 'curl -X GET -H "Content-Type: application/json"  localhost:5001/redfish/v1/Fabrics | jq '
curl -X GET -H "Content-Type: application/json"  localhost:5000/redfish/v1/Fabrics | jq 
