"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:hello tingqi FENG
# 2. Process:The program applies four different string methods to transform the input text in different ways.
# 3. Out:Four transformed versions of the sentence are printed to the screen, one per line.
# 4. My four transformations, and when each is useful:
#    - upper(): converts all letters to uppercase -> useful for banners, titles, or emphasis
#    - replace("FENG", ""): removes a specific word -> useful for filtering out unwanted words
#    - replace("hello", "Bonjour"): swaps one word for another -> useful for basic translation or localization
#    - title(): capitalizes the first letter of each word -> useful for formatting names and headings


# Your code below
input = ("hello tingqi FENG")
#transformation 1: all letters to uppercase
print(input.upper())
#transformation 2: remove a specific word
print(input.replace("FENG", ""))
#transformation 3: swap one word for another
print(input.replace("hello", "Bonjour"))
#transformation 4: capitalize the first letter of each word
print(input.title())