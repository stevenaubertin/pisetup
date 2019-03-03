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

# Setup localization
caller.call('./localization/locale.sh', configs['locale'])
caller.call('./localization/timezone.sh', configs['timezone'])

# Setup Network
caller.call('./network/toggle_ssh.sh', configs['toggle_ssh'])

# Setup Optimization
caller.call('./hardware/disable_swap.sh')
caller.call('./hardware/memsplit.sh', configs['memsplit'])

# Install Packages


# Reboot
os.system('reboot')