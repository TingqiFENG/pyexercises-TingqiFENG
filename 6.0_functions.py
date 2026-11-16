"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""
# Exercise 6.0 — Naming a piece of work
# Name: Tingqi FENG

# 1. In:
# The function receives a list of numbers, like the list
# I created in Exercise 4.0.

# 2. Process:
# It starts with a total of zero.
# It loops through the list and adds each number to the total.

# 3. Out:
# The function returns the sum of all numbers in the list.

# 4. My function name, and why return rather than print:
# calculate_list_total clearly describes what the function does.
# Returning the total allows me to store it, reuse it in another
# calculation, or print it outside the function.
# Printing inside the function alone would only display the value,
# rather than return the calculated result to the caller.

# Empty-list behaviour:
# An empty list returns 0 because there are no numbers to add.
# This is acceptable because the total of an empty list is zero.


# Calculate and return the total of a list of numbers.
def calculate_list_total(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


# Use my original list from Exercise 4.0 and two different inputs.
list_of_numbers = [10, 9, 8, 7, 6, 5]
second_list = [2, 3, 4, 5]
third_list = [-5, 0, 10]


# Call the function three times and store the returned results.
first_total = calculate_list_total(list_of_numbers)
second_total = calculate_list_total(second_list)
third_total = calculate_list_total(third_list)


# Display the three results outside the function.
print("Total of the first list:", first_total)
print("Total of the second list:", second_total)
print("Total of the third list:", third_total)


# Test the function with an empty list.
empty_total = calculate_list_total([])
print("Total of an empty list:", empty_total)