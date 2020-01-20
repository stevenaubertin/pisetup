#!/bin/python

import os
import json
import logging
import sys
from common.caller import Caller

def exit_or_continue():
    i = None
    while i not in ['e', 'c']:
        i = input('exit or continue ? [e/c]')
    if i is 'e':
        sys.exit(0)
    if i == 'c':
        pass

# Loads configurations
with open('./config.json', 'r') as fp:
    configs = json.load(fp)

# Setup logger and helper
logging.basicConfig(format=configs['logformat'], filename=configs['logfile'], level=logging.INFO)
caller = Caller(logging)

# Update
caller.os_call('apt-get update'.split())
exit_or_continue()

# Install some package
caller.call("./git/install.sh")
exit_or_continue()

# Setup localization
caller.call('./localization/locale.sh', configs['locale'])
exit_or_continue()

caller.call('./localization/timezone.sh', configs['timezone'])
exit_or_continue()

# Setup Network
caller.call('./network/toggle_ssh.sh', configs['toggle_ssh'])

# Setup System
caller.call('./hardware/disable_swap.sh')
exit_or_continue()

caller.call('./hardware/memsplit.sh', configs['memsplit'])
exit_or_continue()

# Install Packages
caller.call('./docker/install.sh')
exit_or_continue()
#caller.call('./kubernetes/install.sh')

# Reboot
caller.os_call('reboot')