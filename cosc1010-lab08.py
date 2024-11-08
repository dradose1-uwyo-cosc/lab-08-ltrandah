# Lily Trandahl
# UWYO COSC 1010
# 11/08/2024
# Lab 08
# Lab Section: 13
# Sources, people worked with, help given to: TA's during lab helped, googled clarifying questions, looked thorugh lecture material, asked co worker clarifying questions.
# Project Quirks/ Things that don't work: Couldn't figure out how to get floats to only be one decimal place.

def num_convert(num):
    isNeg = False
    if "-" in num:
        isNeg = True
        num = num.replace("-", "")
    if "." in num:
        num_list = num.split(".")
        if len(num_list) == 2 and num_list[0].isdigit() and num_list[1].isdigit():
            if isNeg:
                return -1 * float(num)
            else: 
                return float(num)
    elif num.isdigit():
        if isNeg:
            return -1 * int(num)
        else: 
            return int(num)
    else: 
        return False

def point_slope(m, b, low_x, up_x):
    points = []
    for x in range (low_x, up_x + 1):
        y = m * x + b
        points.append(y)
        return points

m, b, low_x, up_x = None, None, None, None
while True: 
    m = input("Enter a value for m or type 'exit' to leave: ")
    if m.lower() == "exit":
        break
    m = num_convert(m)
    if m == False:
        continue

    b = input("Enter a value for b or type 'exit' to leave:")
    if b.lower() == "exit":
        break
    b = num_convert(b)
    if b == False:
        continue

    low_x = input("Enter a lower bound or type 'exit' to leave:")
    if low_x.lower() == "exit":
        break
    low_x = num_convert(low_x)
    if low_x == False or low_x is float:
        continue

    up_x = input("Enter an upper bound or type 'exit' to leave:")
    if up_x.lower() == "exit":
        break
    up_x = num_convert(up_x)
    if up_x == False or up_x is float: 
        continue
    num_result = m, b, low_x, up_x
    print(f"The values you have entered for m, b, lower bound, and upper bound are: {num_result}")
    point_slope(m, b, low_x, up_x)
    break

print("*" * 75)

import math
def solve_quad(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    elif discriminant == 0:
        z_root = -b / (2*a)
        return (z_root, z_root)
    elif discriminant < 0:
        return (f"null")
a = float(input("Enter the value for a (coefficient of x^2): "))
b = float(input("Enter the value for b (coefficient of x): "))
c = float(input("Enter the value for c (constant term): "))
quad_ans = solve_quad(a, b, c)    
print(f"The solved quadratic equation based on your input is y = {quad_ans}")

print("*" * 75)

# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
#     m, the slope
#     b, the intercept
#     a lower x bound
#     an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false
# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
# If the number you are trying to take the square root of is negative, return null