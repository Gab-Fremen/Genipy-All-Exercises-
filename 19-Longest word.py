"""
Write a function giving the longest word in a given text.

Your function should be named longest_word, take a single argument text and return a string which should be the longest word in the given text.

Beware: the given text can span several lines.
"""

#define the function to find the longest word in a given text, it should take a parameter text, which is the text to be analyzed, and return the longest word in that text
def longest_word(text):

    #define a variable to store the longest word, and set it to an empty string, and another variable to store the length of the longest word, and set it to 0.
    biggest_word = " "
    longest_len = 0
    
    #Use a for loop to go through the words in the text (replace the new line characters with a space, and split the text by spaces to get the words)
    for word in text.replace("\n", " ").split(" "):
        
        #Use an if statement to check if the length of the word is greater than the length of the longest word, if it is, set the longest word to the current word, and set the length of the longest word to the length of the current word.
        if len(word) > longest_len:
            biggest_word = word
            longest_len = len(word)
            
    return biggest_word
    
#call the function and print the result to the console, you can change the text to test it with different inputs
output_longest_word = longest_word("")
print(output_longest_word)
