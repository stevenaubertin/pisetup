#!/bin/python

import sys
import os
from shutil import copyfile
import argparse


def set_hostname(hostname, keep_backup=True):
    def backup(filename):
        if keep_backup:
            copyfile(filename, filename+'.old')

    hostnamefile = '/etc/hostname'
    if not os.path.exists(hostnamefile):
        raise FileExistsError("Can't find file : "+hostnamefile)
    backup(hostnamefile)
    with open(hostnamefile, 'w') as fp:
        fp.writelines([hostname, os.linesep])

    hostsfile = '/etc/hosts'
    if os.path.exists(hostsfile):
        backup(hostsfile)
        with open(hostsfile, 'w') as fp:
            fp.seek(-len(os.linesep), os.SEEK_END)
            fp.write("127.0.0.1\t"+hostname + os.linesep)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Change hostname of the Pi')
    parser.add_argument('hostname', required=True, type=str, help='the hostname to use')
    parser.add_argument('--backup', type=bool, help='indicate if the original files should be keep')

    args = parser.parse_args()
    set_hostname(args.hostname, args.backup)
    sys.exit(0)
