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
# assume the scripts are invoked from BASE_DIR/sunfish_server/scripts directory
SCRIPT_DIR=$(pwd)
parent="${SCRIPT_DIR%/*}"
WORK_DIR="${parent%/*}"



print_help() {
    cat <<EOF

Helper to relink a Sunfish + 2 Agents emulator to a new Sunfish Core Library build. 
    ../../sunfish_lib:      contains the Core library repo
    ../../sunfish_server:   contains the sunfish server API service (aka Sunfish Core Service)
    ../../agent_1:          if it exists, contains the 1st agent API application (ex. fabric manager)
    ../../agent_2:          if it exists, contains the 2nd agent API application (ex. appliance manager)

USAGE:

    $(basename $0) [--workspace DIR] 

Options:

    -w | --workspace DIR -- Directory to set up the emulator. Defaults to
                            '$WORK_DIR'.


EOF
}

# Extract command line args
while [ "$1" != "" ]; do
    case $1 in
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



# go to sunfish_lib directory and re-make Sunfish library core
echo "re-make Sunfish Core Library"
cd $WORK_DIR/sunfish_lib
echo $(pwd)
. venv/bin/activate
make build
deactivate

# relink the sunfish_server
echo "re-link Sunfish Server"
cd $WORK_DIR/sunfish_server
echo $(pwd)
. venv/bin/activate
pip3 install --force-reinstall ../sunfish_lib/dist/sunfish-0.1.0-py3-none-any.whl
deactivate

# relink the fabric manager server (agent_1)
echo "re-link agent_1 Server"
cd $WORK_DIR/agent_1
. venv/bin/activate
echo $(pwd)
pip3 install --force-reinstall ../sunfish_lib/dist/sunfish-0.1.0-py3-none-any.whl
deactivate

# relink the appliance manager server (agent_2)
echo "re-link agent_2 Server"
cd $WORK_DIR/agent_2
echo $(pwd)
. venv/bin/activate
pip3 install --force-reinstall ../sunfish_lib/dist/sunfish-0.1.0-py3-none-any.whl
deactivate
cd $WORK_DIR


echo ""
echo "fire up the Sunfish API server"
echo "and two instances of Agents"
echo ""
echo "Then 'cd $SCRIPT_DIR' and"
echo "use the shell scripts found there to reset the demo"

exit 0
