#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len_argv = len(sys.argv)
    end_line = ":"
    if (len_argv - 1) == 0:
        end_line = "."
    print("{0} arguments{1}".format(len_argv - 1, end_line))
    for i in range(1, len_argv):
        print("{0}: {1}".format(i, sys.argv[i]))
