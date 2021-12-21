#!/usr/bin/python3
for alpha in range(97, 123):
    """Print all the letters except q and e"""
    if alpha != 113 and alpha != 101:
        print("{:c}".format(alpha), end="")
