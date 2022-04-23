#!/usr/bin/python3
"""
    HOWTO Fetch Internet Resources Using The urllib Package.
"""
from urllib import request, error
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
    try:
        with request.urlopen(pagename) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except error.HTTPError as err:
        print('Error code: {}'.format(err.code))


if __name__ == '__main__':
    url = argv[1]
    result = showcontent(url)
