#!/usr/bin/python

import os
import sys

os.system("chmod +x /boot/PiBakery/blocks/sethostname/sethostname.sh")
os.system("/boot/PiBakery/blocks/sethostname/sethostname.sh "+sys.argv[1])
