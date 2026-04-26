"""
Provide a script printing every possible pairs of two different letters.

Only lower case, one pair per line, ordered alphabetically.

Don't print pairs consisting of twice the same letter, such as 'aa', 'bb', etc...
"""


import string

alphabet = string.ascii_lowercase

for first_letter in alphabet:
    for second_letter in alphabet:
        
#Use an if statement to check if the first letter is different from the second letter, if it is, print the combination of the first and second letter.
        if first_letter != second_letter:
            print(first_letter + second_letter)