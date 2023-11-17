import requests
import sys

requests.packages.urllib3.disable_warnings()

HOST = ""
USER = ""
PASS = ""

def change_hostname(hostname):
    url = "https://{h}/restconf/data/Cisco-IOS-XE-native:native/hostname".format(h=HOST)
    payload = '{{"hostname": "{hn}"}}'.format(hn=hostname)
    send_request(url, payload)

def send_request(url, payload):
    headers = {'Content-Type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}
    response = requests.request("PUT", url, auth=(USER, PASS), data=payload, headers=headers, verify=False)
    print(response.text)

def main():
    hostname = input("Enter the hostname: ")
    change_hostname(hostname)


if __name__ == '__main__':
    sys.exit(main())
