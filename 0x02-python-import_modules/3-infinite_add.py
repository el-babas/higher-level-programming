#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    suma = 0
    name_exec = sys.argv[0]
    for item in sys.argv:
        if name_exec != item:
            suma += int(item)
    print(suma)
