#!/bin/bash
#America/Toronto

timedatectl set-timezone "$1"
dpkg-reconfigure -f noninteractive tzdata