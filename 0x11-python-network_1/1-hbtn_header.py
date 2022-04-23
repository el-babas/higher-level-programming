#!/usr/bin/python3
"""
    HOWTO Fetch Internet Resources Using The urllib Package.
"""
import urllib.request
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
    with urllib.request.urlopen(pagename) as response:
        # Info! Get headers from the pagename
        pageheaders = response.headers
        print(pageheaders.get(key))


if __name__ == '__main__':
    getvalueheaders(argv[1], 'X-Request-Id')
