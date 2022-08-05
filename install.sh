#!/bin/bash

sudo apt-get update && sudo apt-get upgrade -y

sudo apt-get install tree -y
sudo apt-get install wget -y
sudo apt-get install git -y
sudo apt-get install nano -y

curl -sSL get.docker.com | sh && sudo usermod x0r -aG docker

sudo apt-get install libffi-dev libssl-dev
sudo apt install python3-dev
sudo apt-get install -y python3 python3-pip
sudo apt-get install docker-compose -y

sudo systemctl to enable Docker

echo "Change locale and hostname"
sudo raspi-config
