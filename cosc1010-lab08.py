# Lily Trandahl
# UWYO COSC 1010
# 11/07/2024
# Lab 08
# Lab Section: 13
# Sources, people worked with, help given to:
# your
# comments
# here

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
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

def convert(value):
    try: 
        return int(value)
    except ValueError:
        pass
    try: 
        result = float(value)
        return round(result, 1)
    except ValueError: 
        pass
    return False

print("*" * 75)

def point_slope(m, b, low_x, up_x):
    points = []
    for x in range (low_x, up_x + 1):
        y = m * x + b
        points.append(x, y)
    y_val = []
    
    for x in range (low_x, up_x + 1):
        y = m * x + b
        y_val.append(y)
    return y_val
    low_x = int(low_x)
    up_x = int(up_x)
    if low_x > up_x:
        print(f"INVALID: The lower bound is greater than the upper bound.")
        return False
    def type_check(low_x, up_x):
        if type(low_x) == int:
            return True
        else: 
            return False
        if type(up_x) == int:
            return True
        else: 
            return False
        if type(m) == int or float:
            return True
        else: 
            return False
        if type(b) == int or float: 
            return True
        else:
            return False
    y, m, x, b = None, None, None, None
    while y is None or m is None or x is None or b is None:
        if y is None:
            y = input("Enter a y value: ")
        if m is None: 
            m = input("Enter an m value: ")
        if x is None: 
            x = input("Enter an x value: ")
        if b is None:
            b = input("Enter a b value: ")
        if input == (exit.lower()):
            break
        result = [m, b, low_x, up_x]
        print(f"The resulting list of values is: (result)")
        point_slope(m, b, low_x, up_x)
   
        

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
