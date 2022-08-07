# pisetup
## Basic Pi Setup with docker

### choco install rpi-imager
Enable advance options in the imager with CTRL+SHIFT+X
Set default configuration with the imager advance options

### Connect to rapsberry pi
ssh-keygen -R 192.168.1.50 && ssh x0r@192.168.1.50

### Update and upgrade packages
sudo apt-get update && sudo apt-get upgrade -y

### Clone pisetup installation
sudo apt-get install giy -y
git clone https://github.com/stevenaubertin/pisetup'
cd pisetup


