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
        result = '''Body response:
        \t- type: {}
        \t- content: {}
        \t- utf8 content: {}'''.format(type(html), html, html.decode('utf-8'))
        print(result)


if __name__ == '__main__':
    mystatus('https://intranet.hbtn.io/status')
