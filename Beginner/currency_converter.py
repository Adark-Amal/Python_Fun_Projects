"""
A currency converter is an application used to convert the value of one currency into another currency. 
To convert one currency to another, we need to write a program to accept user input where the user will 
enter the amount of money, and then the user has to choose the type of currency the user wants to check the value of.

The steps taken to execute this task are:
1. Import currencyRates from the forex_python library
2. Create an instance of currencyRates
3. Take user inputs for amount, currency from and currency to, from the user
4. Print the converted currency

This task will sharpen your skills on how to import libraries and data types
"""

from forex_python.converter import CurrencyRates

def convert_curr():
    """Function that converts amount from one currency to another

    Args:
        None
    
    Return:
        None: only prints out the results
    """

    # create the currency instance
    curr_instance = CurrencyRates()

    # take user inputs
    amount = int(input("Enter the amount: "))
    from_currency = input("From Currency: ").upper()
    to_currency = input("To Currency: ").upper()

    print(from_currency, " To ", to_currency, amount)

    # perform the conversion
    result = curr_instance.convert(from_currency, to_currency, amount)
    print(result)
