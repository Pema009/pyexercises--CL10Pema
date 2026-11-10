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

# 1. In:
# 2. Process:
# 3. Out:
# 4. What happens on 0, on a negative number, on a very large number:


# Your code below

# 1. In: A whole number N entered by the user.
# 2. Process: Check every number from 1 to N.
# 3. Out: Display whether each number is odd or even.
# 4. Special cases:
# If N is 0, ask for a positive number.
# If N is negative, ask for a positive number.
# If N is 5000, display a message that N is too large.

N = int(input("Enter a number: "))

if N <= 0:
    print("Please enter a positive number.")

elif N > 100:
    print("Number is too large. Enter 100 or less.")

else:
    for number in range(1, N + 1):
        if number % 2 == 0:
            print(number, "is even")
        else:
            print(number, "is odd")
