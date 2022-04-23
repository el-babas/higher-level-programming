#!/usr/bin/python3
"""
    You must use the package requests.
"""
import requests


def GETrequest(pagename):
    """
    Python script that fetches in "url" page.
    """
    myrequest = requests.get(pagename)
    content = myrequest.text
    # Info! Print report status.
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)


if __name__ == '__main__':
    GETrequest('https://intranet.hbtn.io/status')
