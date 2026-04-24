"""
Write a program that finds the sum of all natural numbers below 1000 (< 1000) that are multiples of 3 or 5, and prints it.

If we list all the natural numbers below 20 (<20) that are multiples of 3 or 5, we get 3, 5, 6, 9, 10, 12, 15, 18. The sum of these multiples is 78.

Note that 15 is only counted once.

"""




#define the function to compute the sum of multiples of 3 or 5 in a given range (in this case, we will use it from 0 to 1000, but it can be used for any range by changing the parameters given to the function)
def sum_multiples(start, stop):
#define a variable to store the sum of the multiples of 3 or 5, and set it to 0.
    sum = 0
#Use a for loop to go through the range of numbers from start to stop.
    for i in range(start, stop):
#Use an if statement to check if the number is a multiple of 3 or 5, if it is, add it to the sum variable.
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return(sum)
    
#call the function with the parameters 0 and 1000 to get the sum of multiples of 3 or 5 from 0 to 999, cause the stop parameter does not include the last number.
print(sum_multiples(0, 1000))