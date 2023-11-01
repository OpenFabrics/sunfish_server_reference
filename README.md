# Sunfish_flask_test
This application is a basic HTTP REST Server that can be used to test the sunfishcore library.

## Requirements
The sunfishcore library have to be intalled. To create the .whl installable file of sunfishcore library, follow follow the instructions at:
https://github.com/erika-rosaverde/sunfish_library_reference/blob/main/README.md


# Sunfishcore library installation
Follow the following steps to install the sunfishcore library:
> pip3 install [path_to_sunfishcore_library]/dist/sunfishcore-0.1.0-py3-none-any.whl
> <source flask-test/bin/activate]>
> flask run


## Examples of requests:
	curl -X GET localhost:5000/redfish/v1/<resource path>
	
	curl -X POST \
	-H "Content-Type: application/json" \
	-d @<filename>.json localhost:5000/redfish/v1/<resource path>

	curl -X PUT \
	-H "Content-Type: application/json" \
	-d @<filename>.json localhost:5000/redfish/v1/<resource path>

	curl -X PATCH \
	-H "Content-Type: application/json" \
	-d @<filename>.json localhost:5000/redfish/v1/<resource path>

	curl -X DELETE localhost:5000/redfish/v1/<resource path>
