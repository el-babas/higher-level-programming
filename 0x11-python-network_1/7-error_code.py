#!/usr/bin/python3
"""
    You must use the package requests.
"""
import requests
from sys import argv


def showcontent(pagename):
    """
    Function:
        Python script that takes in a URL, sends a request to the URL
        and displays the body of the response (decoded in utf-8).
    Args:
        pagename (str): The url of the page.
    Return:
        Print the content of the page.
    """
    myrequest = requests.get(pagename)
    if myrequest.status_code == 200:
        print(myrequest.text)
    else:
        print("Error code:", myrequest.status_code)


if __name__ == '__main__':
    url = argv[1]
    result = showcontent(url)
