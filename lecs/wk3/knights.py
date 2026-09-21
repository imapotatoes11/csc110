"""
a_is_knight = True
b_is_knight = True
a_statement = (not a_is_knight) and (not b_is_knight)
if a_is_knight == a_statement:
    print("Valid! A is a knight, B is a knight")
# Check to make sure that the characters match their role
# Print Valid/Invalid

a_is_knight = True
b_is_knight = False
a_statement = (not a_is_knight) and (not b_is_knight)
if a_is_knight == a_statement:
    print("Valid! A is a knight, B is a knave")

a_is_knight = False
b_is_knight = True
a_statement = (not a_is_knight) and (not b_is_knight)
if a_is_knight == a_statement:
    print("Valid! A is a knave, B is a knight")

a_is_knight = False
b_is_knight = False
a_statement = (not a_is_knight) and (not b_is_knight)
if a_is_knight == a_statement:
    print("Valid! A is a knave, B is a knave")

###################

# A says: "C is a Knave"
# B says: "A is a Knight or C is a knight"
# C says: "Neither A nor B is a knight"

a_is_knight = True
b_is_knight = True
c_is_knight = True
a_statement = not c_is_knight
b_statement = a_is_knight or c_is_knight
c_statement = not a_is_knight and not b_is_knight
if a_is_knight == a_statement and b_is_knight == b_statement and c_is_knight == c_statement:
    print("Valid! A is a knight, B is a knight, C is a knight")

a_is_knight = True
b_is_knight = True
c_is_knight = False
a_statement = not c_is_knight
b_statement = a_is_knight or c_is_knight
c_statement = not a_is_knight and not b_is_knight
if a_is_knight == a_statement and b_is_knight == b_statement and c_is_knight == c_statement:
    print("Valid! A is a knight, B is a knight, C is a knave")

a_is_knight = True
b_is_knight = False
c_is_knight = True
a_statement = not c_is_knight
b_statement = a_is_knight or c_is_knight
c_statement = not a_is_knight and not b_is_knight
if a_is_knight == a_statement and b_is_knight == b_statement and c_is_knight == c_statement:
    print("Valid! A is a knight, B is a knave, C is a knight")

a_is_knight = True
b_is_knight = False
c_is_knight = False
a_statement = not c_is_knight
b_statement = a_is_knight or c_is_knight
c_statement = not a_is_knight and not b_is_knight
if a_is_knight == a_statement and b_is_knight == b_statement and c_is_knight == c_statement:
    print("Valid! A is a knight, B is a knave, C is a knave")

a_is_knight = False
b_is_knight = True
c_is_knight = True
a_statement = not c_is_knight
b_statement = a_is_knight or c_is_knight
c_statement = not a_is_knight and not b_is_knight
if a_is_knight == a_statement and b_is_knight == b_statement and c_is_knight == c_statement:
    print("Valid! A is a knave, B is a knight, C is a knight")

a_is_knight = False
b_is_knight = True
c_is_knight = False
a_statement = not c_is_knight
b_statement = a_is_knight or c_is_knight
c_statement = not a_is_knight and not b_is_knight
if a_is_knight == a_statement and b_is_knight == b_statement and c_is_knight == c_statement:
    print("Valid! A is a knave, B is a knight, C is a knave")

a_is_knight = False
b_is_knight = False
c_is_knight = True
a_statement = not c_is_knight
b_statement = a_is_knight or c_is_knight
c_statement = not a_is_knight and not b_is_knight
if a_is_knight == a_statement and b_is_knight == b_statement and c_is_knight == c_statement:
    print("Valid! A is a knave, B is a knave, C is a knight")

a_is_knight = False
b_is_knight = False
c_is_knight = False
a_statement = not c_is_knight
b_statement = a_is_knight or c_is_knight
c_statement = not a_is_knight and not b_is_knight
if a_is_knight == a_statement and b_is_knight == b_statement and c_is_knight == c_statement:
    print("Valid! A is a knave, B is a knave, C is a knave")


# scenario 3 ##############
# A says: If B is a knight, then C is a knight.
# B says: Not both A and C are knights
# C says: A and B are different types
a_is_knight = True
b_is_knight = True
c_is_knight = True
a_statement = not b_is_knight or c_is_knight
b_statement = not (a_is_knight and c_is_knight)
c_statement = a_is_knight != b_is_knight
if a_is_knight == a_statement and b_is_knight == b_statement and c_is_knight == c_statement:
    print("Valid! A is a knight, B is a knight, C is a knight")

a_is_knight = True
b_is_knight = True
c_is_knight = False
a_statement = not b_is_knight or c_is_knight
b_statement = not (a_is_knight and c_is_knight)
c_statement = a_is_knight != b_is_knight
if a_is_knight == a_statement and b_is_knight == b_statement and c_is_knight == c_statement:
    print("Valid! A is a knight, B is a knight, C is a knave")

a_is_knight = True
b_is_knight = False
c_is_knight = True
a_statement = not b_is_knight or c_is_knight
b_statement = not (a_is_knight and c_is_knight)
c_statement = a_is_knight != b_is_knight
if a_is_knight == a_statement and b_is_knight == b_statement and c_is_knight == c_statement:
    print("Valid! A is a knight, B is a knave, C is a knight")

a_is_knight = True
b_is_knight = False
c_is_knight = False
a_statement = not b_is_knight or c_is_knight
b_statement = not (a_is_knight and c_is_knight)
c_statement = a_is_knight != b_is_knight
if a_is_knight == a_statement and b_is_knight == b_statement and c_is_knight == c_statement:
    print("Valid! A is a knight, B is a knave, C is a knave")

a_is_knight = False
b_is_knight = True
c_is_knight = True
a_statement = not b_is_knight or c_is_knight
b_statement = not (a_is_knight and c_is_knight)
c_statement = a_is_knight != b_is_knight
if a_is_knight == a_statement and b_is_knight == b_statement and c_is_knight == c_statement:
    print("Valid! A is a knave, B is a knight, C is a knight")

a_is_knight = False
b_is_knight = True
c_is_knight = False
a_statement = not b_is_knight or c_is_knight
b_statement = not (a_is_knight and c_is_knight)
c_statement = a_is_knight != b_is_knight
if a_is_knight == a_statement and b_is_knight == b_statement and c_is_knight == c_statement:
    print("Valid! A is a knave, B is a knight, C is a knave")

a_is_knight = False
b_is_knight = False
c_is_knight = True
a_statement = not b_is_knight or c_is_knight
b_statement = not (a_is_knight and c_is_knight)
c_statement = a_is_knight != b_is_knight
if a_is_knight == a_statement and b_is_knight == b_statement and c_is_knight == c_statement:
    print("Valid! A is a knave, B is a knave, C is a knight")

a_is_knight = False
b_is_knight = False
c_is_knight = False
a_statement = not b_is_knight or c_is_knight
b_statement = not (a_is_knight and c_is_knight)
c_statement = a_is_knight != b_is_knight
if a_is_knight == a_statement and b_is_knight == b_statement and c_is_knight == c_statement:
    print("Valid! A is a knave, B is a knave, C is a knave")
"""

# === Scenario 3 with loops

for a_is_knight in [True, False]:
    for b_is_knight in [True, False]:
        for c_is_knight in [True, False]:
            a_statement = not b_is_knight or c_is_knight
            b_statement = not (a_is_knight and c_is_knight)
            c_statement = a_is_knight != b_is_knight
            if a_is_knight == a_statement and b_is_knight == b_statement and c_is_knight == c_statement:
                print("Valid! A is a knave, B is a knave, C is a knave")

