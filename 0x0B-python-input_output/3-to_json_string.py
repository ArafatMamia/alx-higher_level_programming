#!/usr/bin/python3
"""
this module contain to_json_string function
"""
import json

def to_json_string(my_obj):
    """ this funtion serialize from object to json representaion """
    return json.dumps(my_obj)
