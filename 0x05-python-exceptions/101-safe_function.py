#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        r = fct(*args)
    except Exception as i:
        sys.stderr.write("Exception: {}\n".format(i))
        r = None

    return (r)
