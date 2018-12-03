#!/bin/python

import os
import sys

filename = sys.argv[1]
args = [str(i) for i in sys.argv[2:]]

os.system(''.join(['sudo chmod u+x ', filename]))
os.system(''.join(['sudo ', filename]+args))
