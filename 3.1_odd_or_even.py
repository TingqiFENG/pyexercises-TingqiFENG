"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:an integer N entered by the user
# 2. Process: The program checks if each number from 1 to N is odd or even
# 3. Out: For each number, it prints whether it is odd or even
# 4. What happens on 0, on a negative number, on a very large number:
#.   If the user types 0,the program will print "the N must at leats 1. Nothing to do."and exit
#    If the user types a negative number, the program will print "the N must be a positive integer. Nothing to do."and exit
#    If the user types a very large number, the program will print all the lines from 1 to N, but it will be slow and may not be practical. The program will print a warning message if N is greater than 1000.


# Your code below
# get input from user
N = input("Enter a number N:")
N = int(N)
if N == 0:
    print("The N must be at least 1. Nothing to do.")
elif N < 0:
    print("The N must be a positive integer. Nothing to do.")
else:
    for i in range(1, N + 1):
        if i % 2 == 0:
            print(f"{i} is even.")
        else:
            print(f"{i} is odd.")