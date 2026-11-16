"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Validate three pieces of information typed by the user, and only save them when all
    three are acceptable.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your three fields, and what makes a value acceptable for each? Write the
       rule in plain English before writing any pattern.

WHAT THE AI CANNOT KNOW
    Your three rules. "A valid email" is not a rule, it is a wish. Say what you accept
    and what you reject, and be ready to defend a borderline case.

WHAT TO WATCH
    An assistant will hand you a pattern that looks like line noise. Do not accept it
    until it has explained it to you piece by piece, and you have written that
    explanation in your own words above it.

CHECK IT YOURSELF
    For each field, prepare one value that must pass and two that must fail. Run all
    nine. Any surprise goes in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# Exercise 10.0 — Checking the shape of text
# Name: Tingqi FENG

# 1. What goes in?
# The user enters a registration ID, a campus email address,
# and a workshop code.

# 2. What happens to it?
# The program removes surrounding whitespace.
# Each value is checked against its own regular expression.
# Invalid values cause the program to ask again.
# A CSV record is saved only after all three values pass.

# 3. What comes out?
# Valid information is appended to 10.0_workshop_registrations.csv.
# Columns: Registration ID, Campus Email, Workshop Code.
# The header is written only if the file is empty.
# The program also displays validation and saving messages.

# 4. My fields and their acceptance rules:
# Registration ID:
# Exactly ST followed by six ASCII digits.
# Uppercase ST is required. Leading zeros are allowed.
#
# Campus email:
# The local part contains 1 to 30 ASCII letters or digits.
# It is followed by exactly @campus.edu in lowercase.
# Dots, spaces, underscores and plus signs are not allowed
# in the local part under this simplified registration rule.
# This checks format, not whether the mailbox actually exists.
#
# Workshop code:
# Exactly MKT- followed by three ASCII digits.
# Uppercase MKT is required. MKT-000 is accepted.
#
# Surrounding whitespace is removed before validation.
# Internal whitespace is not accepted.

# Check it yourself:
# ID: ST001234 passes; st001234 and ST12345 fail.
# Email: alex12@campus.edu passes.
# alex.smith@campus.edu and alex12@example.com fail.
# Workshop: MKT-101 passes; mkt-101 and MKT-10 fail.
# Actual results: all nine validation tests passed.
# Each field accepted its valid example and rejected both invalid examples.
# During manual testing, the email field rejected ST001234 and MKT-101.
# After entering an acceptable email and workshop code,
# the program saved the complete registration successfully.


# Your code below

import csv
import re


# ST is literal uppercase text.
# [0-9] accepts an ASCII digit.
# {6} requires exactly six digits.
ID_PATTERN = r"ST[0-9]{6}"


# [A-Za-z0-9] accepts an ASCII letter or digit.
# {1,30} requires between one and thirty of those characters.
# @campus is literal text.
# \. matches an actual dot, rather than any character.
# edu is the required final text.
EMAIL_PATTERN = r"[A-Za-z0-9]{1,30}@campus\.edu"


# MKT- is literal uppercase text followed by a hyphen.
# [0-9]{3} requires exactly three ASCII digits.
WORKSHOP_PATTERN = r"MKT-[0-9]{3}"


# Check the entire cleaned value, not just a matching section.
def is_valid(value, pattern):
    return re.fullmatch(pattern, value.strip()) is not None


# Run one passing and two failing examples for each field.
def run_tests():
    test_cases = [
        ("Registration ID", ID_PATTERN, "ST001234", True),
        ("Registration ID", ID_PATTERN, "st001234", False),
        ("Registration ID", ID_PATTERN, "ST12345", False),

        ("Campus email", EMAIL_PATTERN, "alex12@campus.edu", True),
        (
            "Campus email",
            EMAIL_PATTERN,
            "alex.smith@campus.edu",
            False
        ),
        ("Campus email", EMAIL_PATTERN, "alex12@example.com", False),

        ("Workshop code", WORKSHOP_PATTERN, "MKT-101", True),
        ("Workshop code", WORKSHOP_PATTERN, "mkt-101", False),
        ("Workshop code", WORKSHOP_PATTERN, "MKT-10", False)
    ]

    passed = 0

    print("--- Nine validation tests ---")

    for field, pattern, value, expected in test_cases:
        actual = is_valid(value, pattern)
        correct = actual == expected

        if correct:
            passed += 1

        status = "PASS" if correct else "FAIL"
        print(
            f"{status}: {field}, {value!r}, "
            f"expected={expected}, actual={actual}"
        )

    print(f"Tests passed: {passed}/{len(test_cases)}\n")

    return passed == len(test_cases)


# Repeat a field's question until the value meets its rule.
def ask_validated(prompt, pattern, error_message):
    while True:
        value = input(prompt).strip()

        if is_valid(value, pattern):
            return value

        print(error_message)


# Append one complete registration with a single header.
def save_registration(registration_id, email, workshop):
    filename = "10.0_workshop_registrations.csv"

    with open(filename, "a+", encoding="utf-8", newline="") as file:
        file.seek(0)
        is_empty = file.read(1) == ""

        writer = csv.writer(file)

        if is_empty:
            writer.writerow([
                "Registration ID",
                "Campus Email",
                "Workshop Code"
            ])

        writer.writerow([registration_id, email, workshop])

    return filename


# Collect all three validated values before saving anything.
def main():
    if not run_tests():
        print("Please fix the failed tests before collecting data.")
        return

    print("Campus Marketing Workshop Registration")

    registration_id = ask_validated(
        "Registration ID: ",
        ID_PATTERN,
        "Use uppercase ST followed by six digits, such as ST001234."
    )

    email = ask_validated(
        "Campus email: ",
        EMAIL_PATTERN,
        "Use 1-30 letters or digits followed by @campus.edu."
    )

    workshop = ask_validated(
        "Workshop code: ",
        WORKSHOP_PATTERN,
        "Use uppercase MKT- followed by three digits, such as MKT-101."
    )

    filename = save_registration(registration_id, email, workshop)
    print(f"\nRegistration saved successfully in {filename}.")


# Report file errors or stop cleanly if input is cancelled.
if __name__ == "__main__":
    try:
        main()
    except OSError as error:
        print("Could not save the registration:", error)
    except (EOFError, KeyboardInterrupt):
        print("\nRegistration cancelled.")
