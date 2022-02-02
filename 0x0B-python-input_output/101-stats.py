#!/usr/bin/python3
""" Functions:
        a) def main()
        b) def reset_statuscode()
        c) def print_report()
"""
import sys


def reset_statuscode():
    """ Function: Resets the quantity to 0 for each statuscode.

    Returns:
        New statuscode dictionary.
    """
    dict_sc = dict()
    dict_sc['200'] = 0
    dict_sc['301'] = 0
    dict_sc['400'] = 0
    dict_sc['401'] = 0
    dict_sc['403'] = 0
    dict_sc['404'] = 0
    dict_sc['405'] = 0
    dict_sc['500'] = 0

    return (dict_sc)


def print_report(dict_sc=dict(), size_files=0):
    """ Function: Print the report for each statuscode
        for 10 lines.

    Args:
        dict_sc (dict): Dictionary of statuscode.
        size_files (int): Sum of the sizefiles.
    """
    print("File size: {:d}".format(size_files))
    for key in sorted(dict_sc.keys()):
        if dict_sc[key] != 0:
            print("{}: {:d}".format(key, dict_sc[key]))


def main():
    """ Function: Script that reads stdin line by line and computes metrics.
        Prints a report every 10 lines of data or
        when the program is stopped (ctrl+c).
    """
    dict_sc = reset_statuscode()
    count_lines = 0
    size_files = 0
    key_statucode = ""
    try:
        for line in sys.stdin:
            if count_lines != 0 and count_lines % 10 == 0:
                print_report(dict_sc, size_files)

            try:
                list_info = [info.strip(" \n") for info in line.split(" ")]
                key_statucode = str(list_info[-2])
                if key_statucode in dict_sc:
                    dict_sc[key_statucode] += 1
                size_files += int(list_info[-1])
            except BaseException:
                pass

            count_lines += 1
    except KeyboardInterrupt:
        print_report(dict_sc, size_files)
        raise
    print_report(dict_sc, size_files)


main()
