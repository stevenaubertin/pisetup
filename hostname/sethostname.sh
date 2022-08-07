#From : https://github.com/davidferguson/pibakery-blocks/blob/master/sethostname/sethostname.sh

sudo raspi-config nonint do_hostname "$1"
sudo hostname -b "$1"
sudo systemctl restart avahi-daemon
