"""The Body Mass Index or BMI is calculated from weight and height of a Person. 
The body mass index is calculated by dividing an individual’s weight in kilograms by their height in meters, 
then dividing the answer again by their height. We will complete this task by performing a couple of steps.

The steps we will perform are:
1. We will take user height in centimeters
2. Then we will take user weight in kilograms
3. We will then convert height to meters
4. Compute the bmi by dividing the weight by the sqaure of the height in meters
5. Print out corresponding strength of the results

This task will sharpen our skills on conditional statements and data types
"""

def bmi_calculator():
    """Function that calculates the bmi of user

    Args:
        None:
    
    Return:
        None: Prints out the bmi as well as the strength
    """

    # take input from the user (height, weight, bmi)
    height = float(input("Enter your height in centimeters: "))
    weight = float(input("Enter your Weight in Kg: "))
    height = height/100
    BMI = weight/(height*height)

    print("Your Body Mass Index is: ", BMI)

    # display the strength of the bmi score
    if(BMI>0):
        if(BMI<=16):
            print("You are severely underweight")
        elif(BMI<=18.5):
            print("You are underweight")
        elif(BMI<=25):
            print("You are Healthy")
        elif(BMI<=30):
            print("You are overweight")
        else: print("You are severely overweight")

    else:("Enter valid details")
