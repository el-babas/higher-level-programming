#!/usr/bin/python3
"""
    You must use the package requests.
"""
import requests
from sys import argv


def connectionGitHub(api, username, password):
    """
    Function:
        Python script that takes your GitHub
        credentials (username and password)
        and uses the GitHub API to display your id.
    Args:
        api (str): GitHub API url.
        username (str): GitHub username.
        password (str): GitHub password (personal access token as password).
    """
    myauthentication = requests.auth.HTTPBasicAuth(username, password)
    myrequest = requests.get(api, auth=myauthentication)
    myjson = myrequest.json()
    print(myjson.get('id'))


if __name__ == '__main__':
    urlapi = 'https://api.github.com/user'
    username = argv[1]
    password = argv[2]
    connectionGitHub(urlapi, username, password)
