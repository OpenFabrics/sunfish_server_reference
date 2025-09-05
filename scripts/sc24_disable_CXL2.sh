#! /bin/bash
cp  ../../sc24_sunfish_server/Resources/Fabrics/Sunfish_*/Switches/CXL2/index.json ./test_patch_switch_CXL2.json
sed -i "s/Enabled/Disabled/" ./test_patch_switch_CXL2.json
cat ./test_patch_switch_CXL2.json
FABRIC_NAME=$(grep -Eo 'Sunfish_...._CXL' test_patch_switch_CXL2.json | head -1)
echo "\n"
echo $FABRIC_NAME
echo "curl -X PATCH -H "Content-Type: application/json" -d@test_patch_switch_CXL2.json localhost:5000/redfish/v1/Fabrics/${FABRIC_NAME}/Switches/CXL2"
curl -X PATCH -H "Content-Type: application/json" -d@test_patch_switch_CXL2.json localhost:5000/redfish/v1/Fabrics/${FABRIC_NAME}/Switches/CXL2 | jq
