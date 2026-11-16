"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# The program receives a list of numbers.

# 2. Process, function by function:
# The first function calculates the sum of the numbers.
# The second function finds the largest number.
# The third function finds the smallest number.
# The fourth function uses all three to create a detailed message.

# 3. Out:
# The program displays a detailed message showing the total,
# largest number, and smallest number in the list.

# 4. The question my fourth function answers:
# What is the total, highest, and lowest number in the list?
# Splitting the work into three functions makes it easier
# to test each calculation separately and find mistakes.


# Your code below
def is_zero(num):
    return num == 0

def is_positive(num):
    return num > 0

def is_even(num):
    return num % 2 == 0

def detailed_message(num):
    if is_zero(num):
        sign = "zero"
    elif is_positive(num):
        sign = "positive"
    else:
        sign = "negative"

    if is_even(num):
        number_type = "even"
    else:
        number_type = "odd"

    return f"The number is {sign} and {number_type}."

print("Is zero:", is_zero(0))
print("Is positive:", is_positive(5))
print("Is even:", is_even(4))

num = int(input("Enter a number: "))
print(detailed_message(num))