#!/usr/bin/python3
"""
This module contain from_json_string function
"""

import json

def from_json_string(my_str):
    """ deseriliaze form json representation to python obj """
    return json.loads(my_str)
