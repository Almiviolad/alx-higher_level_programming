#!/usr/bin/python3
"""Write a Python script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter."""
if __name__ == '__main__':
    import sys
    import requests

    if len(sys.argv) > 1:
        payload = {'q': sys.argv[1]}
    else:
        payload = {'q': ""}
    r = requests.post('http://0.0.0.0\
:5000/search_user', data=payload)
    try:
        response = r.json()
        if response == {}:
            print('No result')
        else:
            print('[{}] {}'.format(response.get('id'), response.get('name')))
    except ValueError:
        print("Not a valid JSON")
