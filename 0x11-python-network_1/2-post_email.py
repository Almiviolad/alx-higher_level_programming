#!/usr/bin/python3
""" a Python script that takes in a URL and an email,
sends a POST request to the passed URL
with the email as a parameter, and displays the body of
the response (decoded in utf-8)"""
if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys
    url = sys.argv[1]
    param = {'email': sys.argv[2]}
    en_param = urllib.parse.urlencode(param).encode('ascii')
    req = urllib.request.Request(url, en_param)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
