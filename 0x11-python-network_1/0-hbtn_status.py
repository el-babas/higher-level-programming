#!/usr/bin/python3
"""
    HOWTO Fetch Internet Resources Using The urllib Package.
"""
import urllib.request


def mystatus(pagename):
    """
    Python script that fetches in "url" page.
    """
    with urllib.request.urlopen(pagename) as response:
        html = response.read()
        # Info! Print report status.
        print("Body response:")
        print("\t- type:", type(html))
        print("\t- content:", html)
        print("\t- utf8 content:", html.decode("utf-8"))


if __name__ == '__main__':
    mystatus('https://intranet.hbtn.io/status')
