"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Text input from the user (their answer to a question).
# 2. Process: - Ask the user a question (e.g., "Do you agree?").
#    - Check if the answer, after cleaning spaces and converting to lowercase, is "yes".
#    - Count how many attempts the user makes.
#    - If the answer is "yes", stop the loop.
#    - If the user reaches the maximum number of attempts without saying "yes", stop the loop anyway.

# 3. Out:
#    A summary printed after the loop ends. It shows:
#    - How many attempts were made.
#    - Whether the user succeeded or hit the attempt limit.

# 4. Stop condition, maximum attempts, and summary content:
#    - Stop condition: User enters "yes" (case-insensitive, spaces ignored).
#    - Maximum attempts: 5
#    - Summary contains: total attempts made, and whether the goal was reached.


max_attempts = 5
attempts = 0
success = False

while attempts < max_attempts:
    answer = input("Do you agree? (yes/no): ")
    attempts = attempts + 1

    # Clean the answer: remove spaces and make it lowercase
    cleaned = answer.strip().lower()

    if cleaned == "yes":
        success = True
        break   # exit the loop early because the condition is met

# After the loop, display the summary
print("--- Summary ---")
print("Total attempts:", attempts)

if success:
    print("Result: You agreed! Loop stopped early.")
else:
    print("Result: Maximum attempts reached without agreement.")

