#!/bin/python

try:
    import configparser
except:
    import ConfigParser as configparser
import sys


def find_hostname(MAC):
    config = configparser.ConfigParser()
    config.read('hosts.conf')
    for section in config:
        for entry in config[section]:
            values = config[section][entry]
            values = values.split(' ')
            ip, mac = values if len(values) == 2 else (values, None)
            if mac and mac.upper() == MAC:
                return {'hostname': entry, 'ip': ip, 'mac': mac}
    return None


if __name__ == "__main__":
    MAC = sys.argv[1:]
    if not MAC:
        print('A MAC address needs to be entered')
        sys.exit(-1)

    hostname = find_hostname(MAC)
    if not hostname:
        print("Unable to retreive hostname")
    print(hostname)

    sys.exit(0)
