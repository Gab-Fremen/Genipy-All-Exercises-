"""
Write a function printing every even numbers in the given range, one number per line.

Your function have to be named print_even_numbers and accept two parameters named start and stop.
"""

#define the function using the parameters to give the first and the last number of the range.
def print_even_numbers(start, stop):
    #Use a for loop to go through the range of numbers from start to stop
    for i in range(start, stop):
        #Use an if statement to check if the number is even, if it is, print it to the console.
        if i % 2 == 0:
            print(i)