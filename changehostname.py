#!/bin/python


def set_hostname(hostname, filepath='/etc/hostname'):
    with open(filepath, 'w') as fp:
        fp.write(hostname)
