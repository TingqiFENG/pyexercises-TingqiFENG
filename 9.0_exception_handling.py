"""Exercise 9.0 — Surviving what you did not expect

Useful for the final exam: two campaigns in the exam dataset have zero conversions.

WHAT THE PROGRAM MUST DO
    Ask the user for a number, divide something by it, and keep running whatever the
    user types. Never crash.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two different failures can happen here, and should they produce the same
       message to the user? Decide before coding.

WHAT THE AI CANNOT KNOW
    Your answer to question 4, and how many attempts you allow before giving up.

    An assistant will often propose catching every error at once. Find out why catching
    each failure separately is better, and write the reason in a comment.

CHECK IT YOURSELF
    Run it with: a normal number, then zero, then the word "abc", then an empty line.
    Four runs, four behaviours, all described in a comment. If any of them stopped your
    program, it is not finished.

DELIVERABLE
    This file, with your comments and your code.
"""

# Exercise 9.0 — Surviving what you did not expect
# Name: Tingqi FENG

# 1. What goes in?
# The user enters a conversion count.
# It must be a finite, non-negative whole number.
# Entering q closes the program.

# 2. What happens to it?
# The program converts the input to a number and validates it.
# It divides a fixed campaign cost of 100 EUR by the count.
# Invalid input and division by zero are handled separately.
# The program allows unlimited attempts until the user quits.

# 3. What comes out?
# A positive conversion count produces a cost per conversion.
# Invalid input produces an explanation and another prompt.
# The program does not create an output file.

# 4. Which two failures can happen?
# ValueError occurs when text such as abc or an empty input
# cannot be converted to a number.
# ZeroDivisionError occurs when the conversion count is zero.
# These failures need different messages because entering
# non-numeric text is different from entering a valid number
# that cannot be used as a divisor.

# Why handle the failures separately?
# Separate exception handlers provide specific, useful messages.
# Catching every exception together could hide programming errors.

# Additional validation:
# Negative counts, fractions, NaN and infinity are rejected.
# EOFError and KeyboardInterrupt allow a clean exit.

# Check it yourself — actual results:
# Input 5 displayed a cost per conversion of 20.00 EUR.
# Input 0 displayed a division-by-zero explanation.
# Input abc displayed an invalid-number message.
# All three tests returned to the input prompt without crashing.

# Empty-input test:
# Expected: display an invalid-number message and ask again.
# Actual test results: empty input displayed the invalid-number message
# and returned to the prompt without crashing.


# Your code below

import math


# Keep asking for input until the user chooses to stop.
def main():
    campaign_cost = 100.0

    print("Cost per Conversion Calculator")
    print(f"Campaign cost: {campaign_cost:.2f} EUR")
    print("Enter q to quit.")

    while True:
        # Read the input and allow an explicit exit.
        user_input = input("\nNumber of conversions: ").strip()

        if user_input.lower() == "q":
            print("Calculator closed.")
            break

        # Convert text to a number and report conversion errors.
        try:
            conversions = float(user_input)
        except ValueError:
            print("Invalid input. Please enter a number, such as 5.")
            continue

        # Reject values that cannot represent a conversion count.
        if not math.isfinite(conversions):
            print("Please enter a finite number, not NaN or infinity.")
            continue

        if conversions < 0:
            print("The conversion count cannot be negative.")
            continue

        if not conversions.is_integer():
            print("Please enter a whole number of conversions.")
            continue

        # Handle division by zero separately from invalid text.
        try:
            cost_per_conversion = campaign_cost / conversions
        except ZeroDivisionError:
            print(
                "Cost per conversion is undefined with zero conversions. "
                "Please enter a number greater than zero."
            )
            continue

        # Display the result, then allow another calculation.
        print(f"Cost per conversion: {cost_per_conversion:.2f} EUR")


# Exit cleanly if input ends or the user presses Ctrl+C.
if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nCalculator closed.")