#!/usr/bin/python3
"""
This module contains To JSON string task
"""

import json

def to_json_string(my_obj):
    """function that returns the JSON representation of an object"""
    return json.dumps(my_obj)
