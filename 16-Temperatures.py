"""
Write functions to convert from Fahrenheit to Celsius and vice-versa.

Your functions should look like:
"""


#define the function to convert from Fahrenheit to Celsius, it should take a parameter temp, which is the temperature in Fahrenheit, and return the temperature in Celsius.
def fahrenheit_to_celsius(temp):
    temp = (temp - 32) * 5/9
    return(temp)

#define the function to convert from Celsius to Fahrenheit, it should take a parameter temp, which is the temperature in Celsius, and return the temperature in Fahrenheit.
def celsius_to_fahrenheit(temp):
    temp = (temp * (9/5)) + 32 
    return(temp)