#!/bin/bash
#America/Montreal

timedatectl set-timezone "$1"
dpkg-reconfigure -f noninteractive tzdata