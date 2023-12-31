#!/usr/bin/python3
"""Defines the text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a given string in file.

    Args:
        filename (str): Name of file.
        search_string (str): String to search for within the file.
        new_string (str): String to insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
