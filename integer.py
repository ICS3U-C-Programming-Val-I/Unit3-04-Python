#!/usr/bin/env python3

# Created By: Val Ijaola
# Date: October 19, 2023
# This program tells you if an integer is positive, negative or neutral.


def main():
    # input - get integer from user.
    user_int = int(input("Enter any integer\n"))

    # process - check if int is positive, negative or neutral.
    if user_int > 0:
        # output - display result
        print(f"{user_int} is positive\n")
    elif user_int < 0:
        # output - display result
        print(f"{user_int} is negative\n")
    else:
        # output - display result
        print(f"{user_int} is neutral\n")


if __name__ == "__main__":
    main()
