# pisetup
## Basic Pi Setup with docker

Install the imager
```
choco install rpi-imager
```

Enable advance options in the imager with **CTRL+SHIFT+X**
Set default configuration with the imager advance options

### Connect to rapsberry pi
```
ssh-keygen -R 192.168.1.50 && ssh x0r@192.168.1.50
```
By default the swarm are *__swarm-1__* while unsetted


### Update and upgrade packages
```
sudo apt-get update && sudo apt-get upgrade -y
```

### Install git
```
sudo apt-get install git -y
```

### Clone pisetup installation
```
git clone https://github.com/stevenaubertin/pisetup && cd pisetup
```

### Set env variables for router username and password
``` 
export USERNAME=
export PASSWORD=
```

### Run the install script
```
chmod u+x install.sh
./install.sh
```

# TL;DR
```
export USERNAME=
export PASSWORD=

sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get install git -y && git clone https://github.com/stevenaubertin/pisetup && cd pisetup && chmod u+x install.sh && ./install.sh
```

## Setting Swarm
### Setup docker swarm on manager
```
sudo docker swarm init --advertise-addr 192.168.1.51
```
### Use the output of the commande on other pi

### Setup the Vizualization service
```
sudo docker service create \
        --name viz \
        --publish 8080:8080/tcp \
        --constraint node.role==manager \
        --mount type=bind,src=/var/run/docker.sock,dst=/var/run/docker.sock \
        alexellis2/visualizer-arm:latest
```
Url
```
http://192.168.1.51:8080
```

### Create a registery
```
docker service create --name registry --publish published=5000,target=5000 registry:2
```
