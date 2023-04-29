#!/usr/bin/python3
"""a Python script that fetches
https://alx-intranet.hbtn.io/status"""
import requests
response = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:")
response = response.text
print(f'\t- type: {type(response)}')
print(f'\t- content: {response}')
