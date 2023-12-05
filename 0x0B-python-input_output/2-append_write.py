#!/usr/bin/python3
"""Defines the file-appending function."""


def append_write(filename="", text=""):
    """Appends string to end of UTF8 text file.

    Args:
        filename (str): Name of file to append to.
        text (str): string to append to file.
    Returns:
        No. of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
