#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len_argv = len(sys.argv)
    argument = "arguments:"
    if len_argv == 1:
        argument = "arguments."
    if len_argv == 2:
        argument = "argument:"
    print("{0} {1}".format(len_argv - 1, argument))
    for i in range(1, len_argv):
        print("{0}: {1}".format(i, sys.argv[i]))
