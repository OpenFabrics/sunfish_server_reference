# Sunfish_flask_test
This application is a basic HTTP REST Server that can be used to test the sunfishcore library.

## Requirements
The sunfishcore library have to be intalled. To create the .whl installable file of sunfishcore library, follow follow the instructions at:
https://github.com/erika-rosaverde/sunfish_library_reference/blob/main/README.md


# Sunfishcore library installation
```commandline
make install-sunfish-library SUNFISH_LIBRARY_PATH=<path to the local sunfish_library_reference>
```
As default `SUNFISH_LIBRARY_REPO_PATH` is set to `"../sunfish_library_reference"`. 
Change the path to the location of the 
[sunfish_library_reference](https://github.com/OpenFabrics/sunfish_library_reference) project on your local system.

**Note:** Follow this [README.md](https://github.com/OpenFabrics/sunfish_library_reference/blob/main/README.md#to-generate-the-installation-file)
to build the sunfish_library_reference Python packages.

# Run Sunfish Server and Agent 

Start the Mock Sunfish server
```commandline
make start-sunfish
```

This starts the Sunfish main server with an empty state. The Sunfish internal state can be visualized via GET requests.
For instance, we can inspect the list of Fabrics exposed by Sunfish. These will be empty at startup time.

To start the agent
```
make start-mock-agent

```

To reset the Redfish trees of both Sunfish and Sunfish Agent execute the following:
```commandline
make reset-trees
```

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
