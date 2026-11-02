from enum import Enum

class Char(Enum):
    WRONG = 0
    MISPLACED = 1
    CORRECT = 2

def check_word(guess: str, word: str) -> list[Char]:
    wordl = [i for i in word]
    out = []
    for i in range(len(guess)):
        if guess[i] == wordl[i]:
            out.append(Char.CORRECT)
            wordl[i] = ""
        elif guess[i] in wordl:
            out.append(Char.MISPLACED)
            wordl[wordl.index(guess[i])] = ""
        else:
            out.append(Char.WRONG)
    return out

if __name__ == "__main__":
    WORD = "crane"
    for i in range(5):
        guess = input(f"Enter a guess ({i + 1}/5): ").lower()
        r = check_word(guess, WORD)
        if all([Char.CORRECT == j for j in r]):
            print("correct")
            exit()
        print(r)
