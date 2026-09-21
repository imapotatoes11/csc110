from enum import Enum

word = 'crane'

guess = input("Enter a guess:")

class Guess(Enum):
    CORRECT = 0
    WRONG = 1
    OUT_OF_PLACE = 2

check = []


if word[0] == guess[0]:
    check.append(Guess.CORRECT)
elif guess[0] in word:
    check.append(Guess.OUT_OF_PLACE)
else:
    check.append(Guess.WRONG)

if word[1] == guess[1]:
    check.append(Guess.CORRECT)
elif guess[1] in word:
    check.append(Guess.OUT_OF_PLACE)
else:
    check.append(Guess.WRONG)

if word[2] == guess[2]:
    check.append(Guess.CORRECT)
elif guess[2] in word:
    check.append(Guess.OUT_OF_PLACE)
else:
    check.append(Guess.WRONG)

if word[3] == guess[3]:
    check.append(Guess.CORRECT)
elif guess[3] in word:
    check.append(Guess.OUT_OF_PLACE)
else:
    check.append(Guess.WRONG)

if word[4] == guess[4]:
    check.append(Guess.CORRECT)
elif guess[4] in word:
    check.append(Guess.OUT_OF_PLACE)
else:
    check.append(Guess.WRONG)

print(check)
