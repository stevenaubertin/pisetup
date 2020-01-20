#!/bin/python

import os
import json
import logging
from common.caller import Caller

# Loads configurations
with open('./config.json', 'r') as fp:
    configs = json.load(fp)

# Setup logger and helper
logging.basicConfig(format=configs['logformat'], filename=configs['logfile'], level=logging.INFO)
caller = Caller(logging)

# Packages
if configs['update'] is True:
    caller.call('./package/update.sh')
if configs['upgrade'] is True:
    caller.call('./package/upgrade.sh')
for package in configs['packages']:
    caller.call('./package/install.sh', package)

# Setup localization
caller.call('./localization/locale.sh', configs['locale'])
caller.call('./localization/timezone.sh', configs['timezone'])

# Setup Network
caller.call('./network/toggle_ssh.sh', configs['toggle_ssh'])

# Setup System
caller.call('./hardware/disable_swap.sh')
caller.call('./hardware/memsplit.sh', configs['memsplit'])

# Install Docker
caller.call('./docker/install.sh')
#caller.call('./kubernetes/install.sh')

# Reboot
caller.os_call('reboot')