"""
Provide a script printing every possible pairs of two letters, only lower case, one by line, ordered alphabetically.

So your output should look like:
"""

#import the string module to use the ascii_lowercase variable, which contains all the lowercase letters of the alphabet.
import string   

alphabet = string.ascii_lowercase

#Use a nested for loop to go through every letter of the alphabet, and print the combination of the first and second letter.
for Firstletter in alphabet:
    for Secondletter in alphabet:
        print(Firstletter + Secondletter)