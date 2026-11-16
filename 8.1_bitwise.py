"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign.

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below
# Exercise 8.1 — Bitwise operators (bonus, not graded)
# Name: Tingqi FENG

# 1. What goes in?
# Three campaign permissions, each represented by a different bit:
# VIEW_CAMPAIGN = 001
# EDIT_CAMPAIGN = 010
# PUBLISH_CAMPAIGN = 100

# 2. What happens to it?
# First, I combine view and edit permissions using bitwise OR.
# Next, I use bitwise AND to check for publish permission.
# Then, I add publish permission using bitwise OR.
# Finally, I remove edit permission using AND with an inverted mask.

# 3. What comes out?
# The program displays the decimal and binary values at each step.
# It also displays whether publish permission is present.
# The final permissions allow viewing and publishing, but not editing.

# 4. What are my permissions about?
# They control access to a digital marketing campaign.
# VIEW_CAMPAIGN allows someone to inspect the campaign.
# EDIT_CAMPAIGN allows someone to change campaign content.
# PUBLISH_CAMPAIGN allows someone to launch the campaign.
# These separate permissions let a manager control each action.

# Check it yourself:
# Read the three bits from left to right as Publish, Edit, View.
# Expected combined permissions: 011.
# Expected publish check: False, with a masked value of 000.
# Expected permissions after adding publish: 111.
# Expected permissions after removing edit: 101.
# Actual result: the binary values matched the expected steps:
# 011, 000, 111 and 101.
# I checked that the final value 101 enables Publish and View,
# while Edit is disabled.


# Your code below

# Assign a separate bit to each campaign permission.
VIEW_CAMPAIGN = 0b001
EDIT_CAMPAIGN = 0b010
PUBLISH_CAMPAIGN = 0b100


# Display a permission value in decimal and three-bit binary.
def display_permissions(label, permissions):
    print(f"{label:<35} {permissions:>7}   {permissions:03b}")


# Explain the binary positions and display the individual permissions.
print("Bit order: Publish | Edit | View")
print("A bit of 1 means the permission is enabled.\n")

print(f"{'Step':<35} {'Decimal':>7}   Binary")
print("-" * 55)

display_permissions("View permission", VIEW_CAMPAIGN)
display_permissions("Edit permission", EDIT_CAMPAIGN)
display_permissions("Publish permission", PUBLISH_CAMPAIGN)


# Combine two permissions using bitwise OR.
permissions = VIEW_CAMPAIGN | EDIT_CAMPAIGN
display_permissions("Combine view and edit", permissions)


# Test whether the third permission is present using bitwise AND.
publish_bits = permissions & PUBLISH_CAMPAIGN
display_permissions("Check publish: masked bits", publish_bits)

has_publish = publish_bits == PUBLISH_CAMPAIGN
print(f"Publish permission present? {has_publish}\n")


# Add publish permission without changing the existing permissions.
permissions = permissions | PUBLISH_CAMPAIGN
display_permissions("Add publish permission", permissions)

has_publish = (
    permissions & PUBLISH_CAMPAIGN
) == PUBLISH_CAMPAIGN
print(f"Publish permission present? {has_publish}\n")


# Remove edit permission while preserving the other permissions.
permissions = permissions & ~EDIT_CAMPAIGN
display_permissions("Remove edit permission", permissions)


# Check the final permissions individually.
print("\nFinal permission checks:")
print(
    "Can view:",
    (permissions & VIEW_CAMPAIGN) == VIEW_CAMPAIGN
)
print(
    "Can edit:",
    (permissions & EDIT_CAMPAIGN) == EDIT_CAMPAIGN
)
print(
    "Can publish:",
    (permissions & PUBLISH_CAMPAIGN) == PUBLISH_CAMPAIGN
)