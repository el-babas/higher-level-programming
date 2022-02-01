#!/usr/bin/python3
import sys
import os
""" Script that adds all arguments to a Python list,
    and then save them to a file
"""


fs_json = __import__('5-save_to_json_file').save_to_json_file
fl_json = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
list_json = []

if os.path.isfile(filename):
    list_json = fl_json(filename)

for item in sys.argv[1:]:
    list_json.append(item)

fs_json(list_json, filename)
