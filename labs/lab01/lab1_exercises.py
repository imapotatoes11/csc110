"""CSC110 Lab 1: Exercises

Complete the TODOs below, in order. See the lab handout for full instructions.

WARNING: Do not modify the comments or variable names in this file -- any
automated marking will look for these exact names.
"""

# =============================================================================
# Q1: Tracing booleans and operators by hand
# =============================================================================
# Before running anything, predict each blank on paper. Then uncomment the
# print statements below (or just try each expression directly in the Python
# console) to check your predictions.

# TODO: write your predictions here, then check them.
# m = 8
# n = 5
# m == 8                        -> True
# m == 8 and n == 5             -> True
# not (m == 5 and n == 8)       -> True
# m != 5 and not n != 5         -> True
#
# x = True + 5
# x                             -> 6
# y = 3 * False and 1 / 0
# y                             -> 0
# z = not x != y
# z                             -> False

# TODO: Add a single `not` somewhere in the line below so that it evaluates
# to False instead of True (don't change any of the True/False values).
trace_expression = True and False or True and not True or False


# =============================================================================
# Q2: Writing your own boolean expressions
# =============================================================================
# A patron can borrow a book if EITHER they are a student in good standing
# OR a faculty member -- AND, regardless of which, they must have fewer than
# 10 items already checked out. REGARDLESS of anything else, borrowing is
# blocked if the book is on the reserve shelf.
#
# Fill in your predicted answer (True/False) for each scenario below BEFORE
# running this file, then run it and check (call can_borrow(...) with each
# row's values in the Python console, or run this file and look at the Q2
# output for the first row).
#
# | is_student | in_good_standing | is_faculty | items_checked_out | on_reserve_shelf | predicted | actual |
# | True       | True             | False      | 3                  | False            |   True       |        |
# | False      | False            | True       | 9                  | False            |   True       |        |
# | True       | False            | False      | 2                  | False            |   False       |        |
# | False      | False            | True       | 1                  | True             |   False       |        |
# | True       | True             | False      | 10                 | False            |   False       |        |
#
# For each row, reassign the 5 input variables to that row's values, then
# write a single boolean expression (no `if`) and assign it to that row's
# can_borrow_case_N variable below. Copy the SAME expression each time --
# only the input values change from row to row.

is_student, in_good_standing, is_faculty, items_checked_out, on_reserve_shelf = True, True, False, 3, False
# TODO: write a single boolean expression (no `if`) and assign it below.
can_borrow_case_1 = ((is_student and in_good_standing) or is_faculty) and (items_checked_out < 10) and not on_reserve_shelf

is_student, in_good_standing, is_faculty, items_checked_out, on_reserve_shelf = False, False, True, 9, False
can_borrow_case_2 = ((is_student and in_good_standing) or is_faculty) and (items_checked_out < 10) and not on_reserve_shelf

is_student, in_good_standing, is_faculty, items_checked_out, on_reserve_shelf = True, False, False, 2, False
can_borrow_case_3 = ((is_student and in_good_standing) or is_faculty) and (items_checked_out < 10) and not on_reserve_shelf

is_student, in_good_standing, is_faculty, items_checked_out, on_reserve_shelf = False, False, True, 1, True
can_borrow_case_4 = ((is_student and in_good_standing) or is_faculty) and (items_checked_out < 10) and not on_reserve_shelf

is_student, in_good_standing, is_faculty, items_checked_out, on_reserve_shelf = True, True, False, 10, False
can_borrow_case_5 = ((is_student and in_good_standing) or is_faculty) and (items_checked_out < 10) and not on_reserve_shelf

# =============================================================================
# Q3: Debugging corner
# =============================================================================
# For each snippet in the lab handout, write the error type and a one-sentence
# explanation as a comment below, then write a corrected version as a
# runnable line of code.

# 1. >>> 7 = total
# TODO: error type + explanation:
# SyntaxError. 7 is not a valid variable name
# TODO: corrected code:
# total = 7

# 2. >>> is_open = true
# TODO: error type + explanation:
# NameError. `true` is not defined; in Python, booleans are capitalized (ie `True` or `False`, NOT `true` or `false`)
# TODO: corrected code:
# is_open = True

# 3. >>> is_valid = (age >= 18) and has_id
# TODO: error type + explanation:
# NameError. the variable `age` was not defined.
# TODO: corrected code:
# age = 18
# has_id = True
# is_valid = (age >= 18) and has_id

# 4. >>> result = 3 and 'yes'
#    >>> result + 1
# TODO: error type + explanation:
# TypeError. the first line results in result being `"yes"`, which is a string; you cannot use the addition operator \
# with a string and an int
# TODO: corrected code:
# result = 3 and 'yes'
# result + str(1)

# 5. >>> flag = 5 > 3 > 'a'
# TODO: error type + explanation:
# TypeError. You cannot use a `>` comparison operator between a string and an int
# TODO: corrected code:
# flag = 5 > 3 > ord('a')


# =============================================================================
# Q4: Reading a proof (Self-Explanation Training)
# =============================================================================
# Proposition: for any integer n, the sum of three consecutive integers n,
# n+1, and n+2 is divisible by 3.
#
# Proof: let n, n+1, and n+2 be three consecutive integers.
# Their sum is n + (n+1) + (n+2) = 3n + 3.
# Since 3n + 3 = 3(n+1) and
# since n+1 is an integer, the sum equals 3 times an integer --
# that is, 3 divides the sum.

# TODO: hypothesis:
# for any integer n, the sum of n, n+1, and n+2 is divisible by 3
# TODO: conclusion:
# the sum of the 3 consecutive integers is divisible by 3
# TODO: self-explanation, line 1 (n + (n+1) + (n+2) = 3n + 3):
# In this line, we use algebra to combine like terms, and compute the constant, yielding 3n+3 as the result
# TODO: self-explanation, line 2 (3n + 3 = 3(n+1)):
# Since all terms are divisible by 3, we extract the factor of 3
# TODO: self-explanation, line 3 (n+1 is an integer, so the sum is 3 times an integer):
# From the previous line, 3(n+1) is essentially (n+1) + (n+1) + (n+1), resulting in a sum that is triple the original n+1
# TODO: self-explanation, line 4 (3 divides the sum):
# Since there are no algebraic errors and the result of simplifying the sum, 3(n+1), has a factor of 3, the sum is divisible by 3.
# TODO: which line does the most "work", and why?
# Line 2 does the most "work", by identifying the factor of 3 from the sum. If a number has a factor n, it is divisible by n,
# creating a significant step into proving the proposition.


# =============================================================================
# Q5: The AGM Inequality, by hand and in Python
# =============================================================================
# By hand (using x=15, y=5, a rectangular garden plot):
# TODO: (a) perimeter (total fencing used):
# P = 2(x+y) = 2(15) + 2(5) = 30 + 10 = 40
# TODO: (b) actual area of the 15 x 5 rectangle:
# A = xy = (15)(5) = 75
# TODO: (c) side length and area of the square using the same perimeter:
# side length = P / 4 = 40 / 4 = 10. A = xy = (10)(10) = 100
# TODO: (d) confirm (b) <= (c):
# (b) = 75, (c) = 100. 75 <= 100 ✓
# TODO: (e) which quantity plays sqrt(xy), and which plays (x+y)/2, in the AGM inequality?
# sqrt(xy) is the side length of the square with the same area as the original rectangle, and (x+y)/2 is the side length
# of the square with the same perimeter as the original rectangle
#
# For the plot with x=15, y=5, compute perimeter, actual_area, and
# max_area_same_perimeter (the area of the SQUARE that uses the same total
# amount of fencing, i.e. the same perimeter) directly below.
# Expected: perimeter=40, actual_area=75, max_area_same_perimeter=100.0

x = 15
y = 5

# TODO: compute perimeter
perimeter = 2 * (x + y)

# TODO: compute actual_area
actual_area = x * y

# TODO: compute max_area_same_perimeter
max_area_same_perimeter = ((x + y) / 2) ** 2


if __name__ == '__main__':
    print('Q1 trace_expression:', trace_expression)
    print('Q2 can_borrow_case_1:', can_borrow_case_1)
    print('Q5 perimeter, actual_area, max_area_same_perimeter:',
          perimeter, actual_area, max_area_same_perimeter)
