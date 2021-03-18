"""
In this task we will write a code to generate the acronym for a sentence. Acronym is basically
the short form of long sequence of words.

Steps:
1. Take input from user
2. Split the input into list of words
3. For each word in the list, select only the first letters
4. Capitalize each letters

This code will help improve your knowledge of string manipulation, list indexing and loops
"""

def acronym():
    """Function that returns the acronym of a long list of words

    Args:
        None
    
    Returns:
        None: only prints the acronym for the words
    """
    # accept user input 
    user_input = input("Please type the words: ")

    # split the words into list of words
    words = user_input.split()
    
    # variable to store the acronyms - declared as empty string
    acron = " "

    # select first letters of each word and capitalize the letters
    for word in words:
        acron = acron + word[0].upper()
    
    print("\nAcronym: {}".format(acron))
    