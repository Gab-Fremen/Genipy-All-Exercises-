"""
Find the distance between the two furthest apart values in a list.

Create a dist function, receiving a list of numbers (integers or floating points), and returning the bigger distance between any two given values, so typically the distance between the biggest and the smallest
"""



#define a function to find the distance between the two furthest apart values in a list, it should take a parameter points, which is the list of numbers to be analyzed
def dist(points):

    #define a variable to store the smallest and the biggest number to perform a subtraction between them
    smallest_number = points[0]
    biggest_number = points[0]

    #Use a for loop to go through the numbers in the list
    for i in points:

        #Check if it's bigger than the biggest number, if it is, set the biggest number to the current number
        if biggest_number < i:
            biggest_number = i

        #and if it's smaller than the smallest number, set the smallest number to the current number
        if i < smallest_number:
            smallest_number = i
            
    #Finally, return the distance between the biggest and the smallest number, which is defined by the subtraction of the biggest number by the smallest number
    return biggest_number - smallest_number