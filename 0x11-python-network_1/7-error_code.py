#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)."""
if __name__ == '__main__':
    import requests
    import requests.exceptions
    import sys
    url = sys.argv[1]
    try:
        req = requests.get(url)
        print(req.text)
        req.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print('Error code: {}'.format(req.status_code))
