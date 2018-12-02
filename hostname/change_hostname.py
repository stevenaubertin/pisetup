#!/bin/python

import os
import sys

os.system('chmod u+x ./change_hostname.sh')
os.system('sudo ./change_hostname.sh '+sys.argv[1])
