"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two values did you pick, and which comparison result surprised you?

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below
# Actual test result: I predicted 10 out of 12 results correctly.
# Exercise 8.0 — Operators (bonus, not graded)
# Name: Tingqi FENG

# 1. What goes in?
# Two strings: "Apple" and "apple".

# 2. What happens to it?
# I compare them using ==, !=, <, <=, > and >=.
# I combine comparison results using and, or and not.
# I compare each actual result with a prediction.

# 3. What comes out?
# A table showing each expression, my prediction,
# its actual result, and whether the prediction was correct.
# The program also displays the total number of correct predictions.

# 4. Which values did I pick, and what surprised me?
# I picked "Apple" and "apple".
# I was surprised that "Apple" < "apple" is True.
# I expected the words to be equal because they have the same letters.
# Python compares strings case-sensitively using Unicode code points.
# Uppercase "A" has a smaller code point than lowercase "a",
# so "Apple" comes before "apple".

# Check it yourself:
# Before running, review and change the predictions below.
# True means I predict the expression will be true.
# False means I predict the expression will be false.
# Actual test result: complete after running the program.


# Your code below

# Choose two strings that differ only in capitalisation.
value_a = "Apple"
value_b = "apple"


# Record predictions before calculating the results.
predictions = [
    False,  # a == b
    True,   # a != b
    True,   # a < b
    True,   # a <= b
    False,  # a > b
    False,  # a >= b
    True,   # (a < b) and (a != b)
    False,  # (a == b) and (a < b)
    True,   # (a == b) or (a < b)
    False,  # (a == b) or (a > b)
    True,   # not (a == b)
    False   # not (a < b)
]


# Calculate all six comparison results.
equal = value_a == value_b
not_equal = value_a != value_b
less_than = value_a < value_b
less_or_equal = value_a <= value_b
greater_than = value_a > value_b
greater_or_equal = value_a >= value_b


# Collect comparisons and examples of all three logical operators.
results = [
    ("a == b", equal),
    ("a != b", not_equal),
    ("a < b", less_than),
    ("a <= b", less_or_equal),
    ("a > b", greater_than),
    ("a >= b", greater_or_equal),
    ("(a < b) and (a != b)", less_than and not_equal),
    ("(a == b) and (a < b)", equal and less_than),
    ("(a == b) or (a < b)", equal or less_than),
    ("(a == b) or (a > b)", equal or greater_than),
    ("not (a == b)", not equal),
    ("not (a < b)", not less_than)
]


# Display a readable table and count correct predictions.
print(f"a = {value_a!r}")
print(f"b = {value_b!r}")
print()

print(
    f"{'Expression':<28}"
    f"{'Prediction':<13}"
    f"{'Actual':<10}"
    f"{'Correct?':<10}"
)
print("-" * 61)

correct_count = 0

for index, (expression, actual) in enumerate(results):
    predicted = predictions[index]
    correct = predicted == actual

    if correct:
        correct_count += 1

    print(
        f"{expression:<28}"
        f"{str(predicted):<13}"
        f"{str(actual):<10}"
        f"{'Yes' if correct else 'No':<10}"
    )

print("-" * 61)
print(f"Correct predictions: {correct_count}/{len(results)}")


# Explain why these strings are ordered differently.
print("\nPython string comparisons are case-sensitive.")
print("Strings are compared lexicographically by Unicode code points.")
print(f"'A': {ord('A')}, 'a': {ord('a')}")
print("Therefore, 'Apple' is less than 'apple'.")