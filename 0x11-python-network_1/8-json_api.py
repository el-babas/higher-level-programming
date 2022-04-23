#!/usr/bin/python3
"""
    HOWTO Fetch Internet Resources Using The urllib Package.
"""
import requests
from sys import argv


def POSTrequestJson(pagename, values, head=None):
    """
    Function:
        Python script that takes in a URL and an email,
        sends a POST request to the passed URL.
    Args:
        pagename (str): The url of the page.
        values (dict): The values sends to the server.
        head (dict): The headers sent to the server.
    Return:
        The result of Json POST request (str).
    """
    if not head:
        myrequest = requests.post(pagename, data=values)
    else:
        myrequest = requests.post(pagename, data=values, headers=head)
    try:
        myjson = myrequest.json()
        if not myjson:
            return ("No result")
        else:
            return ("[{}] {}".format(myjson.get('id'), myjson.get('name')))
    except BaseException:
        return ("Not a valid JSON")


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    values = {'q': ''}
    if len(argv) >= 2:
        values['q'] = argv[1]
    result = POSTrequestJson(url, values)
    print(result)
