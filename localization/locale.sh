#!/bin/bash
#From : https://wiki.debian.org/Locale
#en_CA.UTF-8

sudo sed -i 's/^# *\('"$1"'\)/\1/' /etc/locale.gen
sudo locale-gen --purge
sudo locale-gen "$1 UTF-8"
sudo update-locale LANG="$1"
sudo dpkg-reconfigure -f noninteractive locales

echo "locale will be updated after reboot"
echo "default value : $(cat /etc/default/locale | grep LANG)"
