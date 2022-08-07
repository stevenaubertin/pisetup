#!/bin/python

import sys
from logging import error
from get_devicelist import get_devices
import json


def find_name(mac, statics) -> str:
    r = [i for i in filter(lambda x: x['mac'] == mac, statics)]
    return r[0]['name'] if len(r) > 0 else ''


def main(argv):
    error_message = 'username and password and mac address are required, \nUSAGE :\n python '+__file__.split('\\')[-1]+' <username> <password> <mac>'
    if len(argv) != 3:
        error(error_message)
        sys.exit(-1)
    
    username = argv[0]
    password = argv[1]
    mac = argv[2]

    devices = json.loads(get_devices(username, password))
    hostname = find_name(mac, devices['statics'])
    if hostname is None or hostname == '':
        error('Unable to find hostname for mac address "{}"'.format(mac))

    print(hostname)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
