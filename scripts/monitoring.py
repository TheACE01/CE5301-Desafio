#!/usr/bin/env python

from argparse import ArgumentParser
import requests
import urllib3
import json
import sys
import os
from pprint import pprint

if __name__ == '__main__':

    # Disable SSL Warnings
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    parser = ArgumentParser(description='Select options.')

    # Input parameters
    parser.add_argument('-host', '--host', type=str, required=True,
                        help="The device IP or DN")
    parser.add_argument('-user', '--username', type=str, default='cisco',
                        help="User credentials for the request")
    parser.add_argument('-port', '--port', type=int, default=443,
                        help="Specify this if you want a non-default port")
    parser.add_argument('-pass', '--password', type=str, required=True,
                        help="Specify this if you want a non-default port")
    args = parser.parse_args()

    username = args.username
    host = args.host
    port = str(args.port)
    password = args.password

    url = "https://" + host + ":" + port + "/restconf/data/Cisco-IOS-XE-native:native"

    headers = {
       "Content-Type": "application/yang-data+json",
       "Accept": "application/yang-data+json",
       }
    
    try:
        response = requests.request("GET", url, headers=headers, auth=(username,password), verify=False)
        response.raise_for_status()
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(1)

    pprint(response.json())