"""
The Sequential search algorithm is a searching algorithm. To implement this algorithm, we start by 
searching for the target value from the beginning of the array and continue till we find the target value. 
To implement this algorithm, we need to check each element from the beginning until we find the value we are 
looking for

The steps involved include:
1. Search through a list of items
2. If value or item found, end the search

NB: We can easily use the in keyword on the list to find the item or we use the loop approach

This task will sharpen your skills in loops, and conditional statements
"""

def seq_search(list, item):
    """
    Function that searches through a list of items until an item is found

    Args:
        list: this contains all the items that we will be searching through
        item: this is the item we are looking for
    
    Return:
        None: Only prints true or false if item was found
    """

    """
    if item in list:
        print(True)
    else:
        print(False)
    """
    
    for value in list:
        if value == item:
            print('Yes, item was found!')
            break
    else:
        print("Sorry, item wasn't found!")
            
    
seq_search(range(0, 10), 14)