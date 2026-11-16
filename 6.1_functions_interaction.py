"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# Exercise 6.1 — Small functions working together
# Name: Tingqi FENG

# 1. In:
# The program receives an integer entered by the user.

# 2. Process, function by function:
# is_positive checks whether the integer is greater than zero.
# is_zero checks whether the integer equals zero.
# is_even checks whether the integer is divisible by two.
# detailed_message uses these three functions to build a message.
# An integer that is neither zero nor positive must be negative.

# 3. Out:
# The three small functions return True or False.
# detailed_message returns a message describing the integer's
# sign and whether it is even or odd.

# 4. The question my fourth function answers:
# How can this integer be classified by its sign and parity?
# Separate functions let me test each condition independently.
# This makes it easier to identify which check is incorrect.

# Individual test cases:
# is_positive(4) should return True.
# is_zero(0) should return True.
# is_even(4) should return True.
# Additional tests check negative numbers and False results.

# Zero is classified as even because it is divisible by two.


# Check whether the integer is positive.
def is_positive(num):
    return num > 0


# Check whether the integer is zero.
def is_zero(num):
    return num == 0


# Check whether the integer is even.
def is_even(num):
    return num % 2 == 0


# Combine the three checks into one descriptive message.
def detailed_message(num):
    positive = is_positive(num)
    zero = is_zero(num)
    even = is_even(num)

    if zero:
        message = "The number is zero."
    elif positive:
        message = "The number is positive."
    else:
        message = "The number is negative."

    if even:
        message += " The number is even."
    else:
        message += " The number is odd."

    return message


# Test each small function before using them together.
assert is_positive(4) is True
assert is_positive(-3) is False
assert is_positive(0) is False

assert is_zero(0) is True
assert is_zero(4) is False
assert is_zero(-3) is False

assert is_even(4) is True
assert is_even(3) is False
assert is_even(-4) is True
assert is_even(0) is True

print("All individual function tests passed.")


# Ask the user for an integer and handle invalid input.
while True:
    try:
        number = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Please enter a whole number, such as 4, -3 or 0.")


# Display the result returned by the fourth function.
print(detailed_message(number))