#!/bin/bash

echo '###################################'
echo "hostname"
mac=${python ./network/getmac.py}
hostname=${python ./hostname/get_hostname.py "$USERNAME" "$PASSWORD" $mac}
echo "hostname found is $hostname"
sudo raspi-config nonint do_hostname "$hostname"
sudo hostname -b "$hostname"
sudo systemctl restart avahi-daemon

