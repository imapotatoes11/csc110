# Scenario:
#   A movie theater offers a discount to students and seniors.
#   Visitors receive a discount if:
#       - They are a student OR they are a senior (65+)
#       - AND they have their ID
#       - AND they have not visited more than 5 times

# Task 1: Fill in the table below if you expect each case
# to receive a discount (True) or not (False) based on the
# scenario above.

#| Age | Student |   ID   | Visits | Expected |
#| 10  | True    | False  | 0      | False         |
#| 70  | False   | True   | 3      | True         |
#| 20  | True    | False  | 1      | False         |
#| 67  | False   | False  | 10     | False         |
#| 30  | False   | True   | 6      | False         |

# Task 2: Review the code below and run each case to obtain
#  an empirical set of results.

# Do the results match your expected values?
# If not, edit the code to fix any logical issues.

age = 70
student = False
ID = True
visits = 10

senior = age >= 65

discount = (senior or student) and ID and visits < 5 # AND has higher precedence than OR

print(discount)