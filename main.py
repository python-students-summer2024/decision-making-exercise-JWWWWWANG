"""
The code in this file is given to you.
Run this file to call the functions in solutions.py in a way that makes sense.
Feel free to comment out any of it in order to focus only on the functions you are currently working on.
"""

from solutions import *


def main():
    # make use of the functions in solutions.py

    # print out a friendly welcome
    print("\n--- WELCOME! ---\n")

    # print out the current year
    year = get_year()
    print("\nThe current year is {}!".format(year))

   
    # print out whether it's currently a leap year
    print()
    this_year = get_year()
    if is_leap_year():
        print("{} is a leap year!!!!".format(this_year))
    else:
        print("Sorry.... {} is not a leap year.".format(this_year))

    # print out a farewell message
    print()
    print("--- BYE BYE! ---")


# call the main function
main()
