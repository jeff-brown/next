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


def next_palindrome(num):
    """
    function to figure out the next palindrome given any starting value

    args:
        num(int): the starting number

    returns:
        the next palindrome
    """
    length = len(str(num))
    odd_digits = (length % 2 != 0)
    left_half = get_left_half(num)
    middle = get_middle(num)
    if odd_digits:
        increment = pow(10, length / 2)
        new_num = int(left_half + middle + left_half[::-1])
    else:
        increment = int(1.1 * pow(10, length / 2))
        new_num = int(left_half + left_half[::-1])
    if new_num > num:
        return new_num
    if middle != '9':
        return new_num + increment
    return next_palindrome(round_up(num))


def get_left_half(num):
    """
    function to get the left half of a string representation of a starting
    numerical value.
    """
    print(num)
    return str(num)[:int(len(str(num))/2)]


def get_middle(num):
    """
    function to get the middle of a string representation of a starting
    numberical value
    """
    # (len(str(num)) - 1) / 2
    return str(num)[int((len(str(num)) - 1) / 2)]


def round_up(num):
    """
    round up the starting value to the nearest whole number ending in zero
    """
    length = len(str(num))
    increment = pow(10, ((length / 2) + 1))
    return ((num / increment) + 1) * increment


def main():
    """
    the main function calls the next_palindrome function and prints the result
    """
    num = int(sys.argv[1])
    print(num)
    palindrome = next_palindrome(num)
    print(
        "With a starting value of {}, the next palindrome is {}.".format(
            num, palindrome
        )
    )
    return 0


if __name__ == '__main__':
    sys.exit(main())
