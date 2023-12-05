#!/usr/bin/python3
"""Defines the JSON-to-object function."""
import json


def from_json_string(my_str):
    """Return Python object rep of JSON string."""
    return json.loads(my_str)
