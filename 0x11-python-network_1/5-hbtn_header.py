#!/usr/bin/python3
"""
    You must use the package requests.
"""
import requests
from sys import argv


def getvalueheaders(pagename, key):
    """
    Function:
        Python script that takes in a URL, sends a request
        to the URL and displays the custom value of the
        variable found in the header of the response.
    Args:
        pagename (str): The url of the page.
        key (str): The key find in the header of the response.
    Return:
        The value of the key.
    """
    myrequest = requests.get(pagename)
    myheaders = myrequest.headers
    print(myheaders.get(key))


if __name__ == '__main__':
    getvalueheaders(argv[1], 'X-Request-Id')
