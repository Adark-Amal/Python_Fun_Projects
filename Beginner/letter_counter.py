"""
Counting occurrences of a character in a string means counting all substrings of a character from the 
input string. To count the occurrences of a character, we need to write an algorithm that returns the 
number of times each character appears in the input string. Note that we could use libraries to do this
easily but we won't be using any libraries in this example.

To compute the code for this task, here are the steps:
1. Create a dictionary to contain occurence of each string character
2. Loop through each character
3. Check if character is in dict, if yes, add 1 to the initial number and if not, assign 1 to the character

NB: We can use both the if/else block of code to generate the same output as using the get method

This task will sharpen our skills on loops, dictionaries and string manipulation.
"""

def letter_counter(text):
    """Function that a text and counts the number of occurence of letters in the text

    Args:
        text: text from which we will count the letters
    
    Return:
        None: Only prints out dictionary containing counted letters
    """

    count_dict = {}

    for letter in text:
        count_dict[letter] = count_dict.get(letter, 0) + 1

        """
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1
        """

    print(count_dict)
