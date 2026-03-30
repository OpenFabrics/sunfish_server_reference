#!bash
set -e 
LAUNCH_DIR=$(pwd)
cd ../../
BASE_DIR=$(pwd)
echo $BASE_DIR
# /dev_sc25/all_mains/dev_RsrcUpdate/sunfish_server
gnome-terminal --tab --title="Sunfish" --command="bash -c 'cd ~/dev_sc25/all_mains/dev_RsrcUpdate/sunfish_server; . venv/bin/activate; flask run -p 5000 --debugger;$BASH'"
gnome-terminal --tab --title="Fabric Mgr" --command="bash -c 'cd ~/dev_sc25/all_mains/dev_RsrcUpdate/agent_1; . venv/bin/activate; flask run -p 5001 --debugger;$BASH'"
gnome-terminal --tab --title="Appliance Mgr" --command="bash -c 'cd ~/dev_sc25/all_mains/dev_RsrcUpdate/agent_2; . venv/bin/activate; flask run -p 5002 --debugger;$BASH'"
