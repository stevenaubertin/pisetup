#!/bin/python

import sys
import os


def set_hostname(hostname, filepath='/etc/hostname'):
    with open(filepath, 'w') as fp:
        fp.writelines([hostname, '\n'])

    hostsfile = '/etc/hosts'
    if os.path.exists(hostsfile):
        with open(hostsfile, 'w') as fp:
            fp.seek(-len(os.linesep), os.SEEK_END)
            fp.write("127.0.0.1\t"+hostname + os.linesep)


if __name__ == "__main__":
    args = sys.argv[1:]
    args_size = len(args)
    if args_size == 2:
        set_hostname(args[0], args[1])
    elif args_size == 1:
        set_hostname(args[0])
    else:
        print("""Usage : sudo python changehostname.py hostname [filepath]
        hostname : specify the hostname to use
        filepath : specify the hostname filepath""")
    sys.exit(0)
