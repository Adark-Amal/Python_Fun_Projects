"""
A user’s IP address is defanged to prevent the user from clicking on a malicious link. We do this by
replacing “.” in the user IP address with “[.]”

In this code we going to perform various steps to defang an ip address. The steps are:

1. Take the ip address of the user and save in a variable
2. Split the ip address by the separator
3. Replace the separator with a new separator
4. Return the new ip address

For this code, you will get familiar with string splitting and joining.
"""

def defang_ip(address):
    """Function that takes an ip address and defangs it
    Arg:
        Address: the ip address of the user
    
    Return:
         None: Only prints out defanged user ip address
    """

    try:
        # make sure the argument is a string
        old_address = str(address)
        
        # create a string object
        new_address = ""
        
        # split the address by the separator (.)
        split_address = address.split(".")
        
        # define a new separator and join words by that
        separator = "[.]"
        new_address = separator.join(split_address)
        
        print('Defanged IP Address: {}'.format(new_address))
    
    except:
        print('Please make sure your IP address is correct and try again')

