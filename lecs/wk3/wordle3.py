word = 'crane'
guess = input("Enter a guess: ")

word_ = f"{word}"
check = []

CORRECT = 0
WRONG = 1
OUT_OF_PLACE = 2

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    YELLOW='\033[0;33m'
    BLACK='\033[0;30m'

for i in range(len(word)):
    if word[i] == guess[i]:
        check.append(CORRECT)
    elif guess[i] in word_:
        check.append(OUT_OF_PLACE)
        word_ = word_.replace(guess[i], '', 1)
    else:
        check.append(WRONG)


guess = [i.upper() for i in guess]

for i,j in enumerate(check):
    print(bcolors.ENDC, end='')
    if j == CORRECT:
        print(bcolors.OKCYAN + guess[i], end='')
    elif j == WRONG:
        print(bcolors.ENDC + guess[i], end='')
    elif j == OUT_OF_PLACE:
        print(bcolors.YELLOW + guess[i], end='')
print('')
