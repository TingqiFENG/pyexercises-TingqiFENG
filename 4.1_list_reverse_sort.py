"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The original list from 4.0: [10, 9, 8, 7, 6, 5]
# 2. Process: Display the list in four different orders. Two methods return new lists
#             (original unchanged), and two methods modify the list in place.
# 3. Out: Four reordered versions printed, followed by the original list to prove
#         it survived (after restoring it)
# 4. My four orders, and which ones modify the original:
#    - sorted(original) ascending: Returns a NEW list. Original NOT modified.
#    - sorted(original, reverse=True) descending: Returns a NEW list. Original NOT modified.
#    - .sort() ascending: Modifies the ORIGINAL list in place.
#    - .reverse(): Modifies the ORIGINAL list in place.
#    Note: To prove the original survives at the end, we restore it after in-place changes.

# Your code below
# Original list from exercise 4.0
original_list = [10, 9, 8, 7, 6, 5]

# Create a working copy to demonstrate in-place modifications clearly
work_list = original_list.copy()

# Order 1: sorted() ascending (Returns a new list, original NOT modified)
print("Order 1 (sorted ascending):", sorted(work_list))

# Order 2: sorted() descending (Returns a new list, original NOT modified)
print("Order 2 (sorted descending):", sorted(work_list, reverse=True))

# Order 3: .sort() ascending (Modifies the list IN PLACE)
work_list.sort()
print("Order 3 (.sort() ascending):", work_list)

# Order 4: .reverse() (Modifies the list IN PLACE)
work_list.reverse()
print("Order 4 (.reverse()):", work_list)

# Restore the original list to prove it was not damaged by in-place operations
# Since we used a copy for demonstration, the true original is still intact.
# The last line must display the original list.
print("Original list (must match 4.0):", original_list)