#!/bin/usr/python3
"""
This module contain save_to_json_file function
"""

import json 

def save_to_json_file(my_obj, filename):
    """ write an object to json text file"""
    with open(filename, "w", encoding="utf-8") as a_file:
        json.dump(my_obj, a_file)


