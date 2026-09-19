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

secret_word = 'crane'

# User guessed
guess = input("Please enter a 5-letter word: ") # .lower()

# Tell user "correct word or not"
print("Correct word!" if guess == secret_word else "Incorrect word :/")

# Letter 0: correct, out of place, incorrect
#print(f"Letter 0 is {'correct' if guess[0] == secret_word[0] else ('out of place' if secret_word[0] in guess else 'incorrect...')}")
#is_exact_match_0 = guess[0] == secret_word[0]
#is_letter_in_word_0 = secret_word[0] == guess[0] or secret_word[0] == guess[1] or secret_word[0] == guess[2] or secret_word[0] == guess[3] or secret_word[0] == guess[4]
#print(f"{is_exact_match_0 and 'correct'}{is_letter_in_word_0 and not is_exact_match_0 and 'out of place'}{not is_exact_match_0 and not is_letter_in_word_0 and 'incorrect'}")
is_exact_match_0 = guess[0] == secret_word[0]
is_letter_in_word_0 = (
    guess[0] == secret_word[0]
    or guess[0] == secret_word[1]
    or guess[0] == secret_word[2]
    or guess[0] == secret_word[3]
    or guess[0] == secret_word[4]
    or guess[0] == secret_word[5]
)
is_out_of_place_0 = not is_exact_match_0 and is_letter_in_word_0
is_incorrect_0 = not is_exact_match_0 and not is_letter_in_word_0
# Letter 1: Correct, out of place, incorrect
# Letter 2: Correct, out of place, incorrect
# Letter 3: Correct, out of place, incorrect
# Letter 4: Correct, out of place, incorrect
# Letter 5: Correct, out of place, incorrect

