#!/bin/sh

if [ "$1" == "Update" ]
then
    apt-get update
fi
apt-get -y install "$1"
