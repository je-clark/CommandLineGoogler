import requests
import sys
import pprint
import argparse

def print_info(data):

    print(f'IP address owner is {data.get("net").get("orgRef").get("@name")}')

def main(ip):

    head = {'Accept': r'application/json'}
    url = f'http://whois.arin.net/rest/ip/{ip}'
    r = requests.get(url, headers=head, verify=False)
    if r.status_code != 200:
        raise Exception(f'Error code in response: {r.status_code}')
    else:
        print_info(r.json())
    
if __name__ == "__main__":
    desc = 'ip-whois queries the ARIN WhoIS database to return the company that owns a particular IP address'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('ip_addr', nargs='?', default=sys.stdin.buffer, help='IP address to query', action='store')
    
    args = parser.parse_args()

    if type(args.ip_addr) is str:
        main(args.ip_addr)
    else:
        ip = args.ip_addr.read().decode('ascii').rstrip()
        main(ip)