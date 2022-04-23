#!/usr/bin/python3
"""
    HOWTO Fetch Internet Resources Using The urllib Package.
"""
from urllib import request, parse
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
    data = parse.urlencode(values)
    data = data.encode('ascii')
    if not head:
        myrequest = request.Request(pagename, data)
    else:
        myrequest = request.Request(pagename, data, head)

    with request.urlopen(myrequest) as response:
        body = response.read()
        return (body)


if __name__ == '__main__':
    url = argv[1]
    values = {'email': argv[2]}
    result = POSTrequest(url, values)
    print(result.decode('utf-8'))
