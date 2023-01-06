# Pihole

## Create a stack
https://docs.docker.com/engine/swarm/stack-deploy/
docker-compose build
docker-compose push
docker stack deploy --compose-file docker-compose.yml pihole

## Setup pihole as DNS from router


## Setup password
sudo docker ps
sudo docker exec -it <container-name-from-docker-ps> bash
sudo pihole -a -p


## Update adlist 
https://github.com/d3ward/toolz
https://d3ward.github.io/toolz/adblock
https://raw.githubusercontent.com/d3ward/toolz/master/src/d3host.txt
