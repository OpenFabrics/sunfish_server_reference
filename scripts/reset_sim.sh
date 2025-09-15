 #! /bin/bash
 echo  "curl -X POST -H "Content-Type: application/json" localhost:5000/ResetResources" 
 curl -X POST -H "Content-Type: application/json" localhost:5000/ResetResources

 echo  "curl -X POST -H "Content-Type: application/json" localhost:5001/ResetResources" 
 curl -X POST -H "Content-Type: application/json" localhost:5001/ResetResources

 echo  "curl -X POST -H "Content-Type: application/json" localhost:5002/ResetResources" 
 curl -X POST -H "Content-Type: application/json" localhost:5002/ResetResources

 echo  "curl -X POST -H "Content-Type: application/json"  localhost:5001/AgentRegister" 
 curl -X POST -H "Content-Type: application/json" localhost:5001/AgentRegister

 echo  "curl -X POST -H "Content-Type: application/json"  localhost:5002/AgentRegister" 
 curl -X POST -H "Content-Type: application/json" localhost:5002/AgentRegister

 echo  "curl -X POST -H "Content-Type: application/json"  localhost:5001/AgentUpload" 
 curl -X POST -H "Content-Type: application/json" localhost:5001/AgentUpload

 echo  "curl -X POST -H "Content-Type: application/json"  localhost:5002/AgentUpload" 
 curl -X POST -H "Content-Type: application/json" localhost:5002/AgentUpload

 echo  "curl   localhost:5000/redfish/v1/Fabrics" 
 curl  localhost:5000/redfish/v1/Fabrics

