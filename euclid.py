#!/usr/bin/python3
"""
 File Name : next.py

 This script will determine the next palindrom in a series given any starting
    value.

 Creation date : Tue Dec  7 16:42:41 PST 2021
 Last update : Tue Dec  7 16:42:41 PST 2021

 Created By : Jeff Brown <jeffbr@gmail.com>
 Updated By : Jeff Brown <jeffbr@gmail.com>

 Copyright 2019-2021 Brown Company, Inc. All rights reserved.
"""
import sys


def _get_gcd(m, n):
    """
    recursive function for implementing euclid's algorithm
    """
    r = m % n
    print(f"r={r} m={m}, n={n}")
    if r == 0:
        return n

    return _get_gcd(n, r)


def main():
    """
    the main function calls the next_palindrome function and prints the result
    """
    m = abs(int(round(float(sys.argv[1]))))
    n = abs(int(round(float(sys.argv[2]))))

    if m < n:
        m, n = n, m

    print(f"GCD: {_get_gcd(m, n)}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
