#!/bin/bash
# Copyright (c) 2018-2023, The Storage Networking Industry Association.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# Neither the name of The Storage Networking Industry Association (SNIA) nor
# the names of its contributors may be used to endorse or promote products
# derived from this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
#  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
#  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
#  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
#  THE POSSIBILITY OF SUCH DAMAGE.

# exit on error
set -e 

BASE_DIR=$(pwd)
WORK_DIR=$BASE_DIR/test_SC24


print_help() {
    cat <<EOF

Helper to relink a Sunfish + 2 Agents emulator to a new Sunfish Core Library build. 
    'Appliance manager' agent built from the sunfish_reference_server and linked to the Sunfish Core Lib

USAGE:

    $(basename $0) [--port PORT] [--workspace DIR] 

Options:

    -p | --port PORT     -- Port to run the emulator on. Default is $API_PORT.

    -w | --workspace DIR -- Directory to set up the emulator. Defaults to
                            '$WORK_DIR'.


EOF
}

# Extract command line args
while [ "$1" != "" ]; do
    case $1 in
        -p | --port )
            shift
            API_PORT=$1
            ;;
        -w | --workspace )
            shift
            WORK_DIR=$1
            ;;
        -n | --no-start)
            SETUP_ONLY="true"
            ;;
        *)
            print_help
            exit 1
    esac
    shift
done



# Get and build Sunfish library core
cd $WORK_DIR/sc24_sunfish_lib
. venv/bin/activate
make build
deactivate

# Get the Sunfish Server and build it
cd $WORK_DIR/sc24_sunfish_server
. venv/bin/activate
pip3 install --force-reinstall ../sc24_sunfish_lib/dist/sunfish-0.1.0-py3-none-any.whl
deactivate

# Get the fabric manager server and build it
cd $WORK_DIR/sc24_fabric_manager
# First get the sunfish_server
. venv/bin/activate
# install the library core into the fabric manager server
pip3 install --force-reinstall ../sc24_sunfish_lib/dist/sunfish-0.1.0-py3-none-any.whl
deactivate

# Get the appliance manager server and build it
cd $WORK_DIR/sc24_appliance_manager
. venv/bin/activate
pip3 install --force-reinstall ../sc24_sunfish_lib/dist/sunfish-0.1.0-py3-none-any.whl
deactivate
cd $WORK_DIR


echo ""
echo "fire up the Sunfish API server"
echo "and two instances of Agents"
echo ""
echo "Then 'cd $WORK_DIR/sc24_appliance_manager/templates' and"
echo "use the shell scripts found there to reset the demo"

exit 0
