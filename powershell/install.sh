#!/bin/sh

# From : https://docs.microsoft.com/en-us/powershell/scripting/install/install-raspbian?view=powershell-7.2

###################################
# Prerequisites
# Update package lists
sudo apt-get update

# Install libunwind8 and libssl1.0
# Regex is used to ensure that we do not install libssl1.0-dev, as it is a variant that is not required
sudo apt-get install '^libssl1.0.[0-9]$' libunwind8 -y

###################################
# Download and extract PowerShell
# Grab the latest tar.gz
wget https://github.com/PowerShell/PowerShell/releases/download/v7.2.5/powershell-7.2.5-linux-arm32.tar.gz

# Make folder to put powershell
mkdir ~/powershell

# Unpack the tar.gz file
tar -xvf ./powershell-7.2.5-linux-arm32.tar.gz -C ~/powershell

# Start PowerShell from bash with sudo to create a symbolic link
sudo ~/powershell/pwsh -command 'New-Item -ItemType SymbolicLink -Path "/usr/bin/pwsh" -Target "$PSHOME/pwsh" -Force'

# Now to start PowerShell you can just run "pwsh"
