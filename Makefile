# Copyright IBM Corp. 2023
# This software is available to you under a BSD 3-Clause License.
# The full license terms are available here: https://github.com/OpenFabrics/sunfish_library_reference/blob/main/LICENSE


SUNFISH_LIBRARY_REPO_PATH="../sunfish_library_reference"


all:

install-sunfish-library:
	pip3 install ${SUNFISH_LIBRARY_REPO_PATH}/dist/sunfish-0.1.0-py3-none-any.whl

start-sunfish:
	python app.py

start-mock-agent:
	python mock_agent.py

reset-trees:
	rm -r Sunfish/ && git checkout Sunfish/
	git checkout CXLAgent/EventService/Subscriptions/SunfishServer/index.json