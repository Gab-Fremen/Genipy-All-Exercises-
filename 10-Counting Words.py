"""

Provide a script that prints the number of words in the given paragraph.
I prefilled the answer box with the paragraph, in a variable, but in case you lose it, here it is:

whetting_your_appetite = "Python is an easy to learn, powerful programming language. It has efficient high level data structures and a simple but effective approach to object oriented programming. This tutorial introduces the reader informally to the basic concepts and features of the Python language and system. For a description of standard objects and modules..."

"""

whetting_your_appetite = "Python is an easy to learn, powerful programming language. It has efficient high level data structures and a simple but effective approach to object oriented programming. This tutorial introduces the reader informally to the basic concepts and features of the Python language and system. For a description of standard objects and modules..."

# Enter your code below:

#calling the split() method on the variable to split the paragraph to words, and then calling the len() function to count the number of words, and finally printing the result
print(len(whetting_your_appetite.split()))