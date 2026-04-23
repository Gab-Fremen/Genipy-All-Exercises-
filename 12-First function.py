"""
Write a function computing the perimeter of a circle given its radius.

First read the function tutorial.

Your function should be named circle_perimeter(radius), where the radius parameter is the radius of a cirle.

Your function should return the perimeter of a circle of the given radius.

"""



# Type your code here:
#import the math module to use the value of pi
import math

#Define the function to compute the perimeter of a circle given its radius
def circle_perimeter(radius):
    #Calculate the perimeter of a circle using the formula P = 2.pi.r
    perimeter = radius * 2 * math.pi
    return perimeter

