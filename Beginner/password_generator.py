"""
In this task we will write a code to create a password generator

Steps:
1. Take input from user(length of password)
2. randomly generate password from list of letters, numbers and special characters
3. print results to screen

This code will help improve your knowledge of random library and string manipulation
"""

def password():
    """Function that prints the password which is randomly generated

    Args:
        None
    
    Returns:
        None
    """
    
    # import needed libraries
    import random

    # take user input for length of password
    passlen = int(input("Enter the length of password: "))
    s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

    # randomly generate the password and print results
    p = "".join(random.sample(s, passlen))
    print(p)
