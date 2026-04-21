"""
I've written a function called is_anagram.

This function takes two parameters:

    left: it expects just one word, as a Python str.
    right: it also expects just one word, as a Python str.

the function should return True if the two words are anagrams, False otherwise.

Sadly there's a small error in my implementation (try to submit it if you don't catch it), can you fix it?

"""


"""
Given function with error:
def is_anagram(left, right):
    left_letters = sorted(left)
    right_letters = sorted(right)
    return left_letters = right_letters
"""


def is_anagram(left, right):
    left_letters = sorted(left)
    right_letters = sorted(right)
    return left_letters == right_letters
#the error is that the function is using the assignment operator (=) instead of the equality operator (==)
