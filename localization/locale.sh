#!/bin/bash
#From : https://wiki.debian.org/Locale
#en_CA.UTF-8

sed -i 's/^# *\('"$1"'\)/\1/' /etc/locale.gen
locale-gen --purge
locale-gen "$1 UTF-8"
update-locale LANG="$1"
dpkg-reconfigure -f noninteractive locales