#!/bin/bash

#VARIABLES
memsplitsize=16
loc="en_CA.UTF-8"

# Update packages sources and requirements
sudo apt-get update && sudo apt-get upgrade -y

# Installing Packages
echo '###################################'
echo "Installing Packages"
sudo apt-get install curl -y
sudo apt-get install git -y
sudo apt-get install tree -y
sudo apt-get install wget -y
sudo apt-get install nano -y

# Install Powershell
echo '###################################'
echo "Installing Powershell"
chmod u+x ./powershell/install.sh
./powershell/./install.sh

# Setup default editor
# TODO

# Disable swap
echo Disabling swap
sudo dphys-swapfile swapoff && \
sudo dphys-swapfile uninstall && \
sudo update-rc.d dphys-swapfile remove
echo Adding " cgroup_enable=cpuset cgroup_memory=1 cgroup_enable=memory" to /boot/cmdline.txt

echo '###################################'
echo "Mem split $memsplitsize"
sudo cp /boot/cmdline.txt /boot/cmdline_backup.txt
orig="$(head -n1 /boot/cmdline.txt) cgroup_enable=cpuset cgroup_memory=1 cgroup_enable=memory"
echo $orig | sudo tee /boot/cmdline.txt
sudo raspi-config nonint do_memory_split $memsplitsize

# Install Docker and Docker-Compose
echo '###################################'
echo "Installing docker and docker compose"
curl -sSL get.docker.com | sh && sudo usermod x0r -aG docker
#sudo apt-get install libffi-dev libssl-dev
#sudo apt install python3-dev
#sudo apt-get install -y python3 python3-pip
sudo apt-get install docker-compose -y

echo '###################################'
echo "docker deamon on start"
sudo systemctl start docker

# Setup locals
echo '###################################'
echo "setup locale $loc"
sudo sed -i 's/^# *\('"$loc"'\)/\1/' /etc/locale.gen
sudo locale-gen --purge
sudo locale-gen "$loc UTF-8"
sudo update-locale LANG="$loc"
dpkg-reconfigure -f noninteractive locales
echo "locale will be updated after reboot"
echo "default value : $(cat /etc/default/locale | grep LANG)"

echo '###################################'
echo "hostname"
mac=${python ./network/getmac.py}
hostname=${python ./hostname/get_hostname.py "$USERNAME" "$PASSWORD" $mac}
echo "hostname found is $hostname"
sudo -E raspi-config nonint do_hostname "$hostname"
sudo -E hostname -b "$hostname"
sudo -E systemctl restart avahi-daemon

sudo reboot

