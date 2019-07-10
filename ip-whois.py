import requests
import sys
import lxml.etree as etree

help_text = '''
ip-whois help:

ip-whois querys the ARIN WhoIS database to return the company that owns a particular IP address.

Usage:

ip-whois <IP address> | Returns IP ownership info
ip-whois --help       | Returns this message
'''

if sys.argv[1] == "--help":
    print(help_text)
    sys.exit()

ip = sys.argv[1]


head = {'Accept': r'application/json'}
url = f'http://whois.arin.net/rest/ip/{ip}'
r = requests.get(url, params=head, verify=False)
if r.status_code != 200:
    raise Exception(f'Error code in response: {r.status_code}')
else:
    print(etree.tostring(etree.fromstring(r.content), pretty_print=True).decode('utf-8'))