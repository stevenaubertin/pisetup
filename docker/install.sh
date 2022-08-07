#!/bin/sh

echo "Installing docker"
curl -sSL get.docker.com | sh && sudo usermod pi -aG docker

echo "Installing docker compose"
sudo apt-get install docker-compose -y

echo "docker deamon on start"
sudo systemctl start docker
