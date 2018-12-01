#!/bin/python

import sys


def set_hostname(hostname, filepath='/etc/hostname'):
    with open(filepath, 'w') as fp:
        fp.write(hostname)


if __name__ == "__main__":
        args = sys.argv[1:]
        l = len(args)
        if l == 2:
                set_hostname(args[0], args[1])
        elif l == 1:
                set_hostname(args[0])
        else:
                print("""Usage : sudo python changehostname.py hostname [filepath]
                hostname : specify the hostname to use
                filepath : specify the hostname filepath""")
        sys.exit(0)
