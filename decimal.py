#!/usr/bin/env python3

# created by Youngjun Kim
# created on May 2021
# This program uses user defined functions

import math


def to_round(decimal, digit):

    decimal[0] = float(decimal[0])
    decimal[0] = decimal[0] * 10**digit
    decimal[0] = decimal[0] + 0.5
    decimal[0] = int(decimal[0])
    decimal[0] = decimal[0]/10**digit


def main():
    # this function rounds a number by the user to the digit the user wants

    decimal = []

    # input
    user_decimal = input("Enter the number you want to round: ")
    digit = int(input("Enter how many decimal places you want to round by: "))
    decimal.append(user_decimal)
    to_round(decimal, digit)
    print("The rounded number is {}".format(decimal[0]))


if __name__ == "__main__":
    main()
