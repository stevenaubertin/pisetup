#!/bin/python

import os
import sys

os.system('chmod u+x ./update.sh')
os.system('sudo ./update.sh '+sys.argv[1])
