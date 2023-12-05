#!/usr/bin/python3
"""It defines the file-writing function."""


def write_file(filename="", text=""):
    """Write string to UTF8 text file.

    Args:
        filename (str): The name of file to write.
        text (str): Text to write to the file.
    Returns:
        No. of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
