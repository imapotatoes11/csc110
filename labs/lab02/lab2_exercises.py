"""CSC110 Lab 2: Exercises (Week 2 Review)

Complete the TODOs below, in order. See the lab handout for full instructions.

WARNING: Do not modify the comments or variable names in this file.
Automated marking scripts will look for these exact names.
"""

# =============================================================================
# Q1: Tracing if-statement code by hand
# =============================================================================
# Before running anything, trace each snippet in the handout on paper.
# Each snippet prints a single value each time; write your predicted values for
# `alert` below, then check them by running this file.

# TODO: predicted value of alert with temp=25 -> 1
# TODO: predicted value of alert with temp=35 -> 2

temp = 25
alert = 0
if temp > 20:
    alert = alert + 1
if temp > 30:
    alert = alert + 1
alert_case_1 = alert

temp = 35
alert = 0
if temp > 20:
    alert = alert + 1
if temp > 30:
    alert = alert + 1
alert_case_2 = alert


# TODO: (a) predicted value of discount with price=80, quantity=6  -> Bulk Discount
# TODO: (b) predicted value of discount with price=80, quantity=1  -> Small Order Fee
# TODO: (c) what happens with price=30, quantity=3? (name the error, or the printed value) -> NameError

price, quantity = 80, 6
if price > 50:
    if quantity >= 5:
        discount = "Bulk Discount"
if quantity < 2:
    discount = "Small Order Fee"
discount_case_1 = discount

price, quantity = 80, 1
if price > 50:
    if quantity >= 5:
        discount = "Bulk Discount"
if quantity < 2:
    discount = "Small Order Fee"
discount_case_2 = discount

# Code to trace for case (c) -- not runnable!
# price, quantity = 30, 3
# if price > 50:
#     if quantity >= 5:
#         discount = "Bulk Discount"
# if quantity < 2:
#     discount = "Small Order Fee"
# discount_case_2 = discount


# =============================================================================
# Q2: Writing your own if/elif code
# =============================================================================
# Classify a triangle with side lengths a, b, c as 'Invalid', 'Equilateral',
# 'Isosceles', or 'Scalene'. You MUST use an if/elif/else chain, and the
# ORDER of your conditions matters -- see the handout.
#
# For each of the 5 cases below, reassign a, b, c to that case's values,
# then write an if/elif/else chain (copying the SAME chain each time) that
# assigns the result to that case's triangle_case_N variable.

a, b, c = 3, 4, 5
# TODO: write an if/elif/else chain that checks, IN ORDER:
#   1. whether the sides are invalid (a side <= 0, or two sides are 
#      insufficiently large to match the third)
#   2. whether all three sides are equal (Equilateral)
#   3. whether exactly two sides are equal (Isosceles)
#   4. otherwise, Scalene
# ...assigning the result to triangle_case_1.
if a <= 0 or b <= 0 or c <= 0 or (a + b <= c) or (a + c <= b) or (b + c <= a):
    triangle_case_1 = "Invalid"
elif a == b == c:
    triangle_case_1 = "Equilateral"
elif a == b or b == c or a == c:
    triangle_case_1 = "Isosceles"
else:
    triangle_case_1 = "Scalene"

a, b, c = 5, 5, 5
# TODO: copy your code from above but assign to triangle_case_2
if a <= 0 or b <= 0 or c <= 0 or (a + b <= c) or (a + c <= b) or (b + c <= a):
    triangle_case_2 = "Invalid"
elif a == b == c:
    triangle_case_2 = "Equilateral"
elif a == b or b == c or a == c:
    triangle_case_2 = "Isosceles"
else:
    triangle_case_2 = "Scalene"

a, b, c = 5, 5, 8
# TODO: copy your code from above but assign to triangle_case_3
if a <= 0 or b <= 0 or c <= 0 or (a + b <= c) or (a + c <= b) or (b + c <= a):
    triangle_case_3 = "Invalid"
elif a == b == c:
    triangle_case_3 = "Equilateral"
elif a == b or b == c or a == c:
    triangle_case_3 = "Isosceles"
else:
    triangle_case_3 = "Scalene"

a, b, c = 1, 2, 10
# TODO: copy your code from above but assign to triangle_case_4
if a <= 0 or b <= 0 or c <= 0 or (a + b <= c) or (a + c <= b) or (b + c <= a):
    triangle_case_4 = "Invalid"
elif a == b == c:
    triangle_case_4 = "Equilateral"
elif a == b or b == c or a == c:
    triangle_case_4 = "Isosceles"
else:
    triangle_case_4 = "Scalene"

a, b, c = 2, 2, 4
# TODO: copy your code from above but assign to triangle_case_5
if a <= 0 or b <= 0 or c <= 0 or (a + b <= c) or (a + c <= b) or (b + c <= a):
    triangle_case_5 = "Invalid"
elif a == b == c:
    triangle_case_5 = "Equilateral"
elif a == b or b == c or a == c:
    triangle_case_5 = "Isosceles"
else:
    triangle_case_5 = "Scalene"


# =============================================================================
# Q3: Debugging & Reasoning
# =============================================================================
# For each of the 4 items in the handout, write your answer as a comment
# below. Items 2-3 also ask you to write corrected code -- do that as real,
# runnable code where indicated.

# --- Item 1: converse vs. contrapositive ---
# TODO: is the classmate right? which statement (converse/contrapositive)
# did they actually write? give a counterexample n:
# No. They wrote the converse. a counterexample is n=4, which is divisible by 4 but not 8

# --- Item 2: elif ordering bug ---
# TODO: what does grade_letter(95) return, and is that intended?
# grade_letter(95) returns `Pass`, which is not intended (expected to be `Honours`)
#
# For each of the 3 cases below, reassign score, then write a corrected
# if/elif/else chain (copying the SAME chain each time, checking the more
# restrictive condition first) that assigns the result to that case's
# grade_case_N variable.

score = 95
# TODO: write a corrected if/elif/else chain here, assigning to grade_case_1.
if score >= 90:
    grade_case_1 = "Honours"
elif score >= 50:
    grade_case_1 = "Pass"
else:
    grade_case_1 = "Fail"

score = 89
# TODO: copy your code from above but assign to grade_case_2
if score >= 90:
    grade_case_2 = "Honours"
elif score >= 50:
    grade_case_2 = "Pass"
else:
    grade_case_2 = "Fail"

score = 49
# TODO: copy your code from above but assign to grade_case_3
if score >= 90:
    grade_case_3 = "Honours"
elif score >= 50:
    grade_case_3 = "Pass"
else:
    grade_case_3 = "Fail"


# --- Item 3: De Morgan misapplication ---
# TODO: explain what's wrong with `if not username_valid and not password_valid:`,
# and give a pair of username_valid/password_valid values that behaves
# differently between the buggy and corrected versions.
# The buggy version only rejects when BOTH are invalid; it should reject when EITHER is invalid
# For example, False, True should be rejected, but the buggy condition is False
#
# For each of the 2 cases below, reassign username_valid/password_valid,
# then write the corrected boolean expression (copying the SAME expression
# each time -- use De Morgan's Law, a single expression using `or`, not
# `and`) that assigns the result to that case's login_rejected_case_N
# variable. `login_rejected_case_N` should be True if the login attempt
# should be REJECTED (i.e., it's not the case that both username_valid and
# password_valid are True).

username_valid, password_valid = False, True
# TODO: write the corrected boolean expression here, assigning to login_rejected_case_1.
login_rejected_case_1 = not username_valid or not password_valid

username_valid, password_valid = True, True
# TODO: copy your code from above but assign to login_rejected_case_2
login_rejected_case_2 = not username_valid or not password_valid


# --- Item 4: unreachable-branches trap ---
# TODO: trace the snippet with p, q = False, True -- what happens, and why?
# TODO: what's the simplest fix?
# the code produces a `NameError`. `ans` is never assigned since neither condition branch is executed.
# -> P = False, Q = True
# P and Q = False and True = False
# P or ~Q = False or (not True) = False
# The simplest fix is to replace the line `elif p or not q:` with `elif not p or not q`


# =============================================================================
# Q4: Reading a proof (Self-Explanation Training) -- proof by contrapositive
# =============================================================================
# Proposition: for any integer n, if 3 divides n^2, then 3 divides n.
# (See the handout for the full proof.)

# TODO: hypothesis: 3 divides n^2
# TODO: conclusion: 3 divides n
# TODO: the contrapositive being proved, in your own words: if n isn't divisible by 3, then n^2 isn't divisible by 3.
# TODO: self-explanation (i): why the proof splits into two cases at all: when dividing by 3, the possible remainders are 1 and 2, thus 2 cases.
# TODO: self-explanation (ii): the algebra in Case 1: we set n to be a multiple of 3 with a remainder of 1, then we expand and rearrange n^2 to the form n^2=3m+1 for some m
# TODO: self-explanation (iii): the algebra in Case 2: we set n to be a multiple of 3 with a remainder of 2, then we expand and rearrange n^2 to the form n^2=3m+1 for some m
# TODO: self-explanation (iv): how the two cases combine to finish the proof: the two cases cover all possible cases of the contrapositive. since the comtrapositive is proven, then the original statment is also valid
# TODO: which single fact does the most "work" in this proof, and why?
# The line that combines the two cases explains that the contrapositive is proven, which proves the original proposition.
# This line connects together the singificance of the conclusion from proving the contrapositive.


# =============================================================================
# Q5: De Morgan's Law -- from symbols to code
# =============================================================================
# By hand (write your answers as comments):
# TODO: (a) symbolize the download rule using A, P, T, NOT/AND/OR: NOT (NOT A OR (P AND NOT T))
# TODO: (b) apply De Morgan's Law TWICE to simplify (show both steps):
# -> NOT NOT A AND NOT (P AND NOT T)
# -> A AND (NOT P OR T)
# TODO: (c) in plain English, what does the simplified expression say?
# Allow the download if the subscription is active, and either the video is not premium-only or the user has the paid tier.
#
# | subscription_active | premium_only | paid_tier | predicted | actual |
# | True                 | False        | False     |    True      |        |
# | True                 | True         | True      |    True      |        |
# | True                 | True         | False     |    False      |        |
# | False                | False        | True      |    False      |        |
#
# For each of the 4 scenarios above, reassign the three input variables,
# then write an if/elif/else chain (copying the SAME chain each time, using
# your SIMPLIFIED condition from part (b)) that assigns the result to that
# case's download_case_N variable. Each chain should assign one of exactly:
#   'Cannot download: subscription is not active'
#   'Cannot download: this video requires the paid tier'
#   'Download started'

subscription_active, premium_only, paid_tier = True, False, False
# TODO: write an if/elif/else chain using the simplified condition,
# assigning to download_case_1.
if subscription_active and (not premium_only or paid_tier):
    download_case_1 = "Download started"
elif not subscription_active:
    download_case_1 = "Cannot download: subscription is not active"
else:
    download_case_1 = "Cannot download: this video requires the paid tier"

subscription_active, premium_only, paid_tier = True, True, True
# TODO: copy your code from above but assign to download_case_2
if subscription_active and (not premium_only or paid_tier):
    download_case_2 = "Download started"
elif not subscription_active:
    download_case_2 = "Cannot download: subscription is not active"
else:
    download_case_2 = "Cannot download: this video requires the paid tier"

subscription_active, premium_only, paid_tier = True, True, False
# TODO: copy your code from above but assign to download_case_3
if subscription_active and (not premium_only or paid_tier):
    download_case_3 = "Download started"
elif not subscription_active:
    download_case_3 = "Cannot download: subscription is not active"
else:
    download_case_3 = "Cannot download: this video requires the paid tier"

subscription_active, premium_only, paid_tier = False, False, True
# TODO: copy your code from above but assign to download_case_4
if subscription_active and (not premium_only or paid_tier):
    download_case_4 = "Download started"
elif not subscription_active:
    download_case_4 = "Cannot download: subscription is not active"
else:
    download_case_4 = "Cannot download: this video requires the paid tier"


if __name__ == '__main__':
    print('Q1 alert_case_1:', alert_case_1)
    print('Q1 discount_case_1:', discount_case_1)
    print('Q2 triangle_case_1:', triangle_case_1)
    print('Q3 grade_case_1:', grade_case_1)
    print('Q3 login_rejected_case_1:', login_rejected_case_1)
    print('Q5 download_case_1:', download_case_1)
