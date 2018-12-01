#!/bin/python

import sys


def set_hostname(hostname, filepath='/etc/hostname'):
    with open(filepath, 'w') as fp:
        fp.write(hostname)


if __name__ == "__main__":
        args = sys.argv[1:]
        l = len(args)
        if l > 2 or l < 1:
                print("""Usage : sudo python changehostname.py hostname [filepath]
                \t hostname : specify the hostname to use
                \t filepath : specify the hostname filepath""")
        sys.exit(0)
