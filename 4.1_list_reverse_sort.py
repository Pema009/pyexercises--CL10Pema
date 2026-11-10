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

# 1. In:
# 2. Process:
# 3. Out:
# 4. My four orders, and which ones modify the original:


# Your code below

# 1. In: My original list of numbers from Exercise 4.0.

# 2. Process: Reorder the list in four different ways
# without changing the original list.

# 3. Out: Four reordered lists and the original list.

# 4. My four orders:
# Ascending - smallest to largest.
# Descending - largest to smallest.
# Reversed - last item becomes first.
# Even first - even numbers followed by odd numbers.
# None of these operations modify the original list.

numbers = [3, 5, 6, 7, 8, 9, 11, 13, 15, 17, 1, 2, 4, 6, 8, 10]

original_numbers = numbers.copy()

# 1. Ascending order
ascending = sorted(numbers)
print("Ascending order:", ascending)

# 2. Descending order
descending = sorted(numbers, reverse=True)
print("Descending order:", descending)

# 3. Reverse the original order
reversed_numbers = numbers[::-1]
print("Reversed order:", reversed_numbers)

# 4. Even numbers first
even_first = sorted(numbers, key=lambda x: (x % 2 != 0, x))
print("Even numbers first:", even_first)

# Prove that the original list is unchanged
print("Original list unchanged:", numbers == original_numbers)

# The last line must display the original list
print("Original list:", numbers)
