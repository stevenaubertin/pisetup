import requests
import re
import os
import subprocess

name_regex_str = r"[a-zA-Z0-9]*-?[a-zA-Z0-9]+"
ipv4_regex_str = r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}"
ipv6_regex_str = r"[a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2}"

lease_regex = re.compile(
    "\[('{}','{}','{}')".format(name_regex_str, ipv4_regex_str, ipv6_regex_str), 
    re.IGNORECASE | re.MULTILINE
)
arplist_regex = re.compile(
    "'{}','{}','{}'".format(ipv4_regex_str, ipv6_regex_str, name_regex_str),
    re.IGNORECASE | re.MULTILINE
)
statics_regex = re.compile(
    "{}<{}<{}".format(ipv6_regex_str, ipv4_regex_str, name_regex_str),
    re.IGNORECASE | re.MULTILINE
)

response = requests.request(
    "GET", 
    "https://192.168.1.1/update.cgi?_http_id=TIDc10a77e0747f92d5&_nextwait=1&exec=devlist", 
    headers={ 'Authorization': 'Basic YmFuYW5ldmVydGU6SSBtYW5hZ2UgdGhlIG5ldyBmcnVpdCBiYXNrZXQgY2xvc2VseQ==' }, 
    data = {},
    verify = False
)

devlist = response.text.encode('utf8')
arplist = [str(i).replace("'", '').split(',') for i in arplist_regex.findall(devlist)]
lease = [str(i).replace("'", '').split(',') for i in lease_regex.findall(devlist)]
statics = [str(i).replace("'", '').split('<') for i in statics_regex.findall(devlist)]

def print_part(name, data):
    print(name)
    for i in data:
        print(i)
    print('')

print_part('arplist', arplist)
print_part('lease', lease)
print_part('statics', statics)