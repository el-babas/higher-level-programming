#!/usr/bin/python3
"""
    HOWTO Fetch Internet Resources Using The urllib Package.
"""
import requests
from sys import argv


def POSTrequest(pagename, values, head=None):
    """
    Function:
        Python script that takes in a URL and an email,
        sends a POST request to the passed URL.
    Args:
        pagename (str): The url of the page.
        values (dict): The values sends to the server.
        head (dict): The headers sent to the server.
    Return:
        The result of POST request.
    """
    if not head:
        myrequest = requests.post(pagename, values)
    else:
        myrequest = requests.post(pagename, values, headers=head)
    return (myrequest.text)


if __name__ == '__main__':
    url = argv[1]
    values = {'email': argv[2]}
    result = POSTrequest(url, values)
    print(result)
