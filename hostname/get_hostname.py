import requests
from requests.auth import HTTPBasicAuth
import re
import json

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

basic = HTTPBasicAuth('a', 'lol')
response = requests.get('https://192.168.1.1/status-devices.asp?_=1659816271622', auth=basic, verify=False)

devlist = response.text
arplist = [str(i).replace("'", '').split(',') for i in arplist_regex.findall(devlist)]
lease = [str(i).replace("'", '').split(',') for i in lease_regex.findall(devlist)]
statics = [str(i).replace("'", '').split('<') for i in statics_regex.findall(devlist)]

arp = [{i[-1]:{j for j in i[:-1]}} for i in arplist]
#print(arp)
a = {}
for d in arp:
    k = [*d][0] # stupid python way of getting first keys
    values = d[k]
    if k in a.keys():
        a[k].append(values)
    else:
        a[k] = [values]

print(a)

#arp2 = arp
#print(arp2)
exit()
print(lease)
print(statics)
exit()
result = json.dumps({
    'arplist': {i[-1]:i[:-1] for i in arplist},
    'lease': {i[-1]:i[:-1] for i in lease},
    'statics': {i[-1]:i[:-1] for i in statics}
})

print(result)
