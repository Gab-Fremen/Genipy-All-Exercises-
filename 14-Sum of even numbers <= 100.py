"""
Provide a script that prints the sum of every even numbers in the range [0; 100].
"""


#define the function to compute the sum of even numbers in a given range (in this case, we will use it from 0 to 100, but it can be used for any range by changing the parameters given to the function).
def sum_of_even_numbers(start, stop):
    #define a variable to store the sum of the even numbers, and set it to 0.
    sum = 0
    #Use a for loop to go through the range of numbers from start to stop, and use an if statement to check if the number is even, if it is, add it to the sum variable.
    for i in range(start, stop):
        if i % 2 == 0:
            sum += i
    return(sum)
    
    
#call the function with the parameters 0 and 101 to get the sum of even numbers from 0 to 100, cause the stop parameter does not include the last number.
print(sum_of_even_numbers(0, 101))