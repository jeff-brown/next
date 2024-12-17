#!/usr/bin/python3
"""
 File Name : pyramid.py

 Implementation of a pyramid algorithm; where the input is a string of chars
 and the output is the same string in pyramid format padded with '*' on the
 last row.

 Input: 'abcdefghijk'
 Output:
 a
 bc
 def
 ghij
 k****

 Creation date : Tue Dec  7 16:42:41 PST 2021
 Last update : Tue Dec  7 16:42:41 PST 2021

 Created By : Jeff Brown <jeffbr@gmail.com>
 Updated By : Jeff Brown <jeffbr@gmail.com>

 Copyright 2019-2025 Brown Company, Inc. All rights reserved.
"""
import sys


def pyramid(inp: str = "") -> None:
    """
    figure out the pyramid and print it
    """
    if not inp:
        return

    inpl: list = [x for x in inp]
    index: int = 1

    while inpl:
        for _ in range(index):
            print(inpl.pop(0), end="")
        print()
        index += 1
        if inpl and index > len(inpl):
            inpl += '*' * (index - len(inpl))


def main() -> None:
    """
    gets the input string from the cli and calls the pyramid formatter
    """
    inp: str = sys.argv[1]
    pyramid(inp)


if __name__ == '__main__':
    sys.exit(main())
