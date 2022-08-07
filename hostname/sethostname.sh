#From : https://github.com/davidferguson/pibakery-blocks/blob/master/sethostname/sethostname.sh

raspi-config nonint do_hostname "$1"
hostname -b "$1"
systemctl restart avahi-daemon
