#-----------------------------------------------------------------------------
# Name:        Calling Functions (calling_functions.py)
# Purpose:     Demonstrating main code that calls the same functions several
#              times with different parameters, and why returning beats
#              printing
#
# Author:      Mr. Kowalczewski
# Created:     28-Sept-2026
# Updated:     28-Sept-2026
#-----------------------------------------------------------------------------

# All functions go at the top of the program, just below your header (even if you're not using them yet)
# Functions should have a description (after the name and parameters), as well as comments explaining the code within.

def late_calculator(grade, lates=0):
    '''Calculates a student's grade, subtracting marks based on their
       number of lates. Default value of 0 is given for lates.
    '''
    # Return None for an invalid grade
    if (grade < 0 or grade > 100) or lates < 0:
        return None

    # Take off 5% per late and return
    lates_deduction = lates * 5
    grade = grade - lates_deduction
    return grade


def greeting(name, greet='Hello'):
    '''Returns a personalized greeting.'''
    # Create greeting message and return
    message = greet + " " + name
    return message


def calculate_pizza(size, toppings):
    '''Returns the cost of a pizza, based on size and number of toppings.'''
    # return None for invalid parameters
    if (size != 'small' and size != 'medium' and size != 'large') or toppings < 0:
        return None

    # base price depends on size
    if size == 'small':
        base = 2
    elif size == 'medium':
        base = 5
    else:
        base = 10

    # each topping costs 2
    total = base + (toppings * 2)
    return total


# --- Using functions appropriately -------------------------------------------
# Calculating Billy's grade depending on how many lates he has
print("You have a student named Billy in your class, his grade is currently 90%")
billy_lates = int(input("How many times was Billy late this week? "))
billy_grade = late_calculator(90, billy_lates)


# Showing Billy's new grade
print(f"Billy's new grade is: {billy_grade}%")

# Applying one late to his grade
print("Oh no! It's raining today and Billy was late again.")
billy_grade = late_calculator(billy_grade, 1)
print(f"Billy's new grade is: {billy_grade}%")

# Checking if he's happy with his grade
if billy_grade < 70:
    print("He will not be happy with his grade anymore")


# --- Why return? -------------------------------------------------------------
# storing the result in a variable gives much more flexibility
late_student_grade = late_calculator(80, 10)
print(f"Your new grade will be {late_student_grade}%")

grade_difference = 80 - late_student_grade
print(f"This student lost {grade_difference}%")

if late_student_grade < 50:
    print("This student is no longer passing")


