#!/bin/python

import os
import json


directory="./pisetup/"
config_path = directory+'config.json'


def call(cmd, message=None, verbose=True):
    if message : print(message)
    v = 'Success'
    if os.system(cmd) != 0:
        v = 'Error while executing "{}"'.format(cmd)
    if verbose:
        print(v)
        print()


def call_file(filepath, message=None):
    os.system('sudo chmod u+x {}'.format(filepath))
    if './' not in filepath:
        filepath = './' + filepath
    call('{}'.format(filepath), message)


# Packages
call('sudo apt-get update && sudo apt-get upgrade -y', 'Updating packages')

# Setup Git
call_file('{}git/install.sh'.format(directory), 'Setup Git')

# Clone repository
call('git clone https://github.com/stevenaubertin/pisetup', 'Clone repository')

# Loads configurations
try:
    print('Loading Configuration')
    with open(config_path, 'r') as fp:
        configs = json.load(fp)
except:
    raise('Error while loading configuration {}'.format(config_path))
print('Done\n')

# Installing packages
for package in configs['packages']:
    call('sudo apt-get install {} -y'.format(package), 'Installing {}'.format(package))
print()

# Installing Powershell
call_file('{}powershell/install.sh'.format(directory), 'Installing Powershell')

# Setup System
print('Setup System')
call('{}system/disable_swap.sh'.format(directory), 'Disabling swap')
call('{}system/memsplit.sh {}'.format(directory, configs['memsplit']), 'Memsplit {}'.format(configs['memsplit']))
print()

# Installing Docker and friends
call_file('{}docker/install.sh'.format(directory), 'Installing Docker and Friends')

# Setup locals
call_file('{}localization/locale.sh'.format(directory), 'Setup locals')

# Get Mac Address
call('mac=$(python {}network/getmac.py)'.format(directory), 'Get Mac Address')

