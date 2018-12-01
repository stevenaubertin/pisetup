#!/bin/python

import sys
import os
import subprocess


def changepythonversion():
    currentversion = sys.version_info[0]
    print("Python version is "+str(currentversion))

    if currentversion < 3:
        pythons = filter(lambda x: 'python' in x and '.' in x and '-' not in x and 'm' not in x, os.listdir('/usr/bin/'))
        if 'python3.7' not in pythons:
            subprocess.check_output('./installpython37.sh')

        subprocess.check_call('update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1'.split(' '))
        subprocess.check_call('update-alternatives --install /usr/bin/python python /usr/bin/python3.7 2'.split(' '))


if __name__ == "__main__":
    print(changepythonversion())
    sys.exit(0)
