"""
Write a Python program displaying the number of seconds in 365 days.

You'll need the print function to display the result.

You'll need the * operator for the multiplications.

"""

#Define the variable for the number of days, hours, minutes, and seconds
days_in_a_year = int(365)
hours_in_a_day = int(24)
minutes_in_a_hour = int(60)
seconds_in_a_minute = int(60)

#Define the function to calculate the number of seconds in a year
def seconds_in_a_year():
    x = days_in_a_year * hours_in_a_day * minutes_in_a_hour * seconds_in_a_minute
    return x

#Call the function and print the result
print(seconds_in_a_year())