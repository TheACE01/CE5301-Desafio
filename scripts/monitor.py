#!/usr/bin/env python

# This script retrieves entire configuration from a network element via RESTCONF 
# and prints it out in a "pretty" JSON tree.

from argparse import ArgumentParser
import requests
import urllib3
import json
import sys
import os
from getpass import getpass
from pprint import pprint

if __name__ == '__main__':

    # Disable SSL Warnings
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    # Set up sandbox crenentials for the device
    username = ""
    host = ""
    port = ""
    password = ""

    # Define the JSON RESTCONF headers
    headers = {
       "Content-Type": "application/yang-data+json",
       "Accept": "application/yang-data+json",
       }
    
    # Continuous Monitoring
    while True:
        print("1. Get Running Configuration")
        print("2. Get Interfaces Configuration")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        # Monitor choice
        if choice == '1':
            try:
                url = "https://" + host + ":" + port + "/restconf/data/Cisco-IOS-XE-native:native"
                response = requests.request("GET", url, headers=headers, auth=(username,password), verify=False)
                response.raise_for_status()
            except Exception as e:
                print(e, file=sys.stderr)
                sys.exit(1)
        
        # Interfaces Configuration  
        elif choice == '2':
            try:
                url = "https://" + host + ":" + port + "/restconf/data/ietf-interfaces:interfaces"
                response = requests.request("GET", url, headers=headers, auth=(username,password), verify=False)
                response.raise_for_status()
            except Exception as e:
                print(e, file=sys.stderr)
                sys.exit(1)
        elif choice == '3':
            sys.exit(0)
        
        # Undefined choice
        else:
            print("Invalid choice.")
        
        # Print the response  
        pprint(response.json())
