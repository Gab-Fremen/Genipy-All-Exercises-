"""

Find the biggest value in a given list.

Try it by using only a temporary variable, a for loop, and an if to compare the values.

"""
the_list = [
    143266561,
    1738152473,
    312377936,
    1027708881,
    1871655963,
    1495785517,
    1858250798,
    1693786723,
    374455497,
    430158267,
]

#define a variable to store the max value, and set it to the first value of the list.
max_value = the_list[0]

#define a for loop that goes through each value in the list and compares it to the max value, if the value is bigger than the max value, set the max value to that value.
for value in the_list:
    if value > max_value:
        max_value = value
        
#print the max value to the console.
print(max_value)
