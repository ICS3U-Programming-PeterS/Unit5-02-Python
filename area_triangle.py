#!/usr/bin/env python3

# Created by: Peter
# Created on: Mov 24 2022
# This program calculates the area of a triangle using functions


def calculate_area(height, base):
    # get the height and base

    # calculate the area of the triangle with the input
    area = (height * base) / 2

    # output the calculated area
    print("The area is {0} cm²".format(area))


def main():
    # get the height and base
    height_from_user_string = input("Enter the height of a triangle (cm): ")
    base_from_user_string = input("Enter the base of a triangle (cm): ")
    print()

    try:
        # converts the height and base to floats
        height_float = float(height_from_user_string)
        base_float = float(base_from_user_string)

        # makes sure input is greater than 0
        if base_float > 0 and height_float > 0:
            # call the function to calculate the area
            calculate_area(height_float, base_float)
        else:
            # The inputs can't be negative or zero
            print("The base and height must be greater than 0.")
    # checks if the number is a string
    except Exception:
        print("Only numbers can be accepted!")


if __name__ == "__main__":
    main()
