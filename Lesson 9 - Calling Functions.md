# Lesson 9 - Calling Functions

The example code for this lesson is in `calling_functions.py`. Open it
alongside these notes and run it as we go.

To call a function, use its name followed by any required parameters in
brackets. We saw this last lesson.

The point of a function is reusable code. It is only worthwhile if we call it
several times with different parameters, for different results.

Some students do this when they first write functions:

```python
def my_function(parameter1):
    # Calculates... something I don't know
    expression = parameter1 * 5 - 8
    return expression


# Main Code

# calling the function, storing the result in a variable
result = my_function(10)
print(f"The value of the function is {result} with a parameter of 10")

# Move on with program and never use function again.
```

What is the point of that function? It may organize the program a little, but
if it is used once you might as well write the code directly.

A good function is used several times to produce different results.

## Using functions appropriately

Below are two functions from last lesson, `late_calculator()` and `greeting()`,
plus a new one, `calculate_pizza()`. The main code (the code that runs when we
run the program) makes several uses of `late_calculator()` with different
results.

```python
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


# Calculating Billy's grade depending on how many lates he has
print("You have a student named Billy in your class, his grade is currently 90%")
billy_lates = int(input("How many times was Billy late this week? "))
billy_grade = late_calculator(90, billy_lates)


# Showing Billy's new grade
print(f"Billy's new grade is: {billy_grade}%")

# Applying one late to his grade
print("Oh no! It's raining today and Billy was late.")
billy_grade = late_calculator(billy_grade, 1)
print(f"Billy's new grade is: {billy_grade}%")

# Checking if he's happy with his grade
if billy_grade < 70:
    print("He will not be happy with his grade anymore")

```

## Why return?

Last lesson said it is better to return a value than to print it. Consider this
version:

```python
def late_calculator(grade, lates=0):
    # check for an invalid grade
    if (grade < 0 or grade > 100) or lates < 0:
        print("Error grade must be positive")

    # Take off 5% per late and print
    lates_deduction = lates * 5
    grade = grade - lates_deduction
    print(f"Your new grade will be {grade}%")

# This prints the message above, but also prints None.
# Without a return value, Python returns None by default.
print(late_calculator(80, 2))
```

This function can be called many times with different parameters, but it can
only do one thing: print that exact message.

Now return the result instead, and see what we can do with the value:

```python
def late_calculator(grade, lates=0):
    # Return None for an invalid grade
    if (grade < 0 or grade > 100) or lates < 0:
        return None

    # Take off 5% per late and return
    lates_deduction = lates * 5
    grade = grade - lates_deduction
    return grade

# storing the result in a variable gives much more flexibility
late_student_grade = late_calculator(80, 10)
print(f"Your new grade will be {late_student_grade}%")

grade_difference = 80 - late_student_grade
print(f"This student lost {grade_difference}%")

if late_student_grade < 50:
    print("This student is no longer passing")
```

## Calling a Function Multiple Times

Some students will do the following in their programs:

```python
for i in range(0, 10):
    myFunction(8, i)
    
# move on and never use the function again
```

This is technically calling the function multiple times, and with different parameters (getting different results).  But the question is: if you're never going to call the function again in your program, why not just include the function code inside the loop?  What's the point of the function?

To make the **best possible use** of functions in your programs, you should make different function calls in various places.  In the large example above you can see two different function calls, in different places.  This means that you have avoided re-writing the same code in two different places - not something you can say if you're using a loop!

## Functions summarized

- Functions let you write code once and use it many times. This saves time,
  reduces errors and organizes your program.
- Functions receive information from parameters (not from `input()`), do some
  quick work and return the result. Returning gives you more options than
  printing.
- A function is worthwhile when it is used several times with different
  parameters for different results.
- Repeating the same function call inside a loop is not a good use of a
  function. Why not put that code in the loop instead?
- You can `print()` inside a function, but then every call prints that message.
  Return the result instead, and do whatever you like with it.

## Lab

That is it for the lesson. Move on to Lab 9, in `README.md`.
