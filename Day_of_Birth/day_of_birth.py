import datetime
import calendar


# birth day function
def day_of_birth(date):
    """This function returns the day of birth based on the birth date
    Arg:
        date: date of birth
    Return:
        day of birth
    """
    # convert date to datetime object
    birth_date = datetime.datetime.strptime(date, "%d/%m/%Y")

    # extract the weekday and return the calender day
    day = birth_date.weekday()
    return calendar.day_name[day]


# take input from user for their birth date in the defined format
user_date = input("Please enter your birth date (day/month/year): ")

print("Your day of birth is {}".format(day_of_birth(user_date)))
