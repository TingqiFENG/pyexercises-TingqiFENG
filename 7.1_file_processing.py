"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# Exercise 7.1 — Loading, cleaning and sorting names
# Name: Tingqi FENG

# Problems observed in names.txt:
# 1. Lines 3 and 9 are empty.
# 2. Some names have unnecessary leading spaces.
# 3. Capitalisation is inconsistent across the names.
# 4. Guido van Rossum has a multi-word surname, so using only
#    the final word would give the wrong surname sorting key.

# 1. What goes in?
# The input is names.txt, containing one name per non-empty line.
# The supplied file has 10 lines, including two empty lines.

# 2. What happens to it?
# Empty lines: skip them.
# Unnecessary whitespace: split and rejoin the words.
# Inconsistent capitalisation: capitalise the name words.
# Multi-word surname: preserve "van Rossum" as the surname.
# Sort the cleaned records by their complete surname.

# 3. What comes out?
# A new file named names_cleaned.txt containing eight names,
# sorted by surname, with one name per line.
# The original names.txt is not modified.

# 4. What does sorting by last name mean?
# For two-word names in this file, the first word is the given
# name and the second word is the surname.
# For Guido van Rossum, "van Rossum" is the complete surname.
# I sort this surname under V, including the particle "van".
# This rule is specific to the supplied data, not every culture.

# Check it yourself:
# Expected input: 10 lines.
# Expected output: 8 lines.
# The difference is caused by removing two empty lines.
# Expected first name: Margaret Hamilton.
# Expected last name: Guido van Rossum.
# Actual result: complete this comment after running and checking.

# Actual result: 10 input lines became 8 output lines.
# Two empty lines were removed.
# I checked the order: Margaret Hamilton is first,
# and Guido van Rossum is last.
# Your code below

from pathlib import Path


# Clean one line and return its display name and surname.
def clean_name(line):
    words = line.split()

    if not words:
        return None

    if len(words) < 2:
        raise ValueError(f"Incomplete name: {line!r}")

    # Handle the multi-word surname found in this particular file.
    if [word.casefold() for word in words] == [
        "guido", "van", "rossum"
    ]:
        return ("Guido van Rossum", "van Rossum")

    # Standardise the remaining two-word names.
    if len(words) != 2:
        raise ValueError(f"Please check this name's format: {line!r}")

    first_name = words[0].capitalize()
    last_name = words[1].capitalize()

    return (f"{first_name} {last_name}", last_name)


# Load the input, remove empty lines and sort by surname.
def main():
    folder = Path(__file__).resolve().parent
    input_path = folder / "names.txt"
    output_path = folder / "names_cleaned.txt"

    with input_path.open(encoding="utf-8-sig") as file:
        original_lines = file.readlines()

    records = []
    empty_lines = 0

    for line in original_lines:
        record = clean_name(line)

        if record is None:
            empty_lines += 1
        else:
            records.append(record)

    # Use the complete surname as the main sorting key.
    records.sort(
        key=lambda record: (
            record[1].casefold(),
            record[0].casefold()
        )
    )

    # Write only to the new output file.
    with output_path.open("w", encoding="utf-8") as file:
        for full_name, surname in records:
            file.write(full_name + "\n")

    # Reopen the output to check its actual line count.
    with output_path.open(encoding="utf-8") as file:
        output_lines = file.readlines()

    print("Original lines:", len(original_lines))
    print("Empty lines removed:", empty_lines)
    print("Output lines:", len(output_lines))

    if records:
        print("First name:", records[0][0])
        print("Last name:", records[-1][0])

    print("Saved in:", output_path.name)
    print("The original file was not modified.")


# Display a clear message if the file cannot be processed.
if __name__ == "__main__":
    try:
        main()
    except (OSError, UnicodeError, ValueError) as error:
        print("Could not process the names:", error)