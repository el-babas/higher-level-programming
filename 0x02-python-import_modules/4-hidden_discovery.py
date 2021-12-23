#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hid
    for item in dir(hid):
        if item[0:2] != "__":
            print(item)
