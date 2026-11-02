"""CSC110 Lab 6: Exercises (Week 6 Review)

Complete the TODOs below, in order. See the lab handout for full instructions.

WARNING: Do not modify the comments or variable names in this file except to fill
in the requested answers and to remove a TODO once you have finished a task.
Automated marking scripts will look for these exact names.
"""

# =============================================================================
# Q1: Tracing scope by hand
# =============================================================================
# : predicted print(n) in Snippet A -> 10
# : predicted print(result) in Snippet A -> 20
# : predicted print(changed) in Snippet B -> apple
# : predicted print(secret_word) in Snippet B -> crane


# --- Snippet A 
n = 10

def double(n):
    n = n * 2
    return n

result = double(n)
print(n)       # ?
print(result)  # ?

# --- Snippet B 
secret_word = 'crane'

def change_secret(new_secret):
    secret_word = new_secret
    return secret_word

changed = change_secret('apple')
print(changed)       # ?
print(secret_word)   # ?

# =============================================================================
# Q2: Wordle helpers via the Function Design Recipe
# =============================================================================

def is_valid_guess(guess: str, word_length: int) -> bool:
    """Return whether guess has exactly word_length characters.

    >>> is_valid_guess('crane', 5)
    True
    >>> is_valid_guess('ball', 5)
    False
    """
    # : implement
    return len(guess) == word_length


def score_guess(guess: str, secret: str) -> list[str]:
    """Return per-position Wordle feedback for guess against secret.

    Each entry is 'Correct', 'Out of place', or 'Incorrect', using the
    two-phase algorithm from the Week 3/4 Wordle scripts (exact matches
    first, then consume still-available secret letters).

    Preconditions: len(guess) == len(secret); both are lowercase.

    >>> score_guess('crane', 'crane')
    ['Correct', 'Correct', 'Correct', 'Correct', 'Correct']
    >>> score_guess('pappa', 'apple')
    ['Out of place', 'Out of place', 'Correct', 'Incorrect', 'Incorrect']
    """
    # : implement
    out = ['Incorrect'] * len(guess)
    q = [i for i in secret]

    for i in range(len(guess)):
        if guess[i] == secret[i]:
            out[i] = 'Correct'
            q[i] = ''

    for i in range(len(guess)):
        if out[i] == 'Incorrect' and guess[i] in q:
            out[i] = 'Out of place'
            j = q.index(guess[i])
            q[j] = ''

    return out



# =============================================================================
# Q3: Debugging & Reasoning
# =============================================================================

# --- Item 1: missing return ---
# : what does the buggy version actually return, and why?
# The buggy version returns `None`. If no return statement is written, the funciton implicitly returns `None`.

def is_valid_guess_fixed(guess: str, word_length: int) -> bool:
    """Return whether guess has exactly word_length characters.

    >>> is_valid_guess_fixed('crane', 5)
    True
    >>> is_valid_guess_fixed('hi', 5)
    False
    """
    # : write a corrected version (remember to return!)
    return len(guess) == word_length


# --- Item 2: scope/shadowing ---
max_guesses = 6

# : why is a local `max_guesses = 6` assignment a maintainability trap?
# The local `max_guesses = 6`` shadows the global variable. If the global value changes to 7, the function would still use 6, creating inconsistent behaviour.

def guesses_remaining_fixed(guesses_used: int) -> int:
    """Return how many guesses remain, using the global max_guesses.

    >>> guesses_remaining_fixed(2)
    4
    """
    # : implement using the global max_guesses (no local assignment).
    return max_guesses - guesses_used


# --- Item 3: duplicate-letter scoring bug ---
def naive_score_guess(guess: str, secret: str) -> list[str]:
    """Buggy scorer: does not consume secret letters. Provided for Q3/Q5."""
    messages = []
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            messages.append('Correct')
        elif guess[i] in secret:
            messages.append('Out of place')
        else:
            messages.append('Incorrect')
    return messages


# : naive_score_guess('pappa', 'apple') returns `['Out of place', 'Out of place', 'Correct', 'Out of place', 'Out of place']``
# : correct score_guess('pappa', 'apple') returns `['Out of place', 'Out of place', 'Correct', 'Incorrect', 'Incorrect']`

explain_duplicate_letter_bug = 'The naive scorer counts the same secret letter multiple times because it does not consume letters after matching them'  # : one sentence


# --- Item 4: type-contract mismatch ---
# : what exception does the buggy concatenation raise?
# The buggy function raises a `TypeError`` because it tries to concatenate a string with an integer.

def format_guess_number_fixed(guesses_used: int) -> str:
    """Return a label like 'Guess 3/6'.

    >>> format_guess_number_fixed(3)
    'Guess 3/6'
    """
    # : write a corrected version.
    return 'Guess ' + str(guesses_used) + '/6'


# =============================================================================
# Q4: Functions as relations — injective and surjective
# =============================================================================
# A = {a, b, c}, B = {1, 2, 3}
# f(a)=1, f(b)=2, f(c)=1
# : (a) f as a set of pairs: {(a,1),(b,2),(c,1)}
# : (a) image of f: {1,2}
# : (a) injective? No, since f(a)=f(c)=1 but a != c
# : (a) surjective? No, since 3 is in B but not in the image of f

def is_injective(pairs: set) -> bool:
    """Return whether the function given by pairs is injective.

    You may assume each input appears in at most one pair.

    >>> is_injective({('a', 1), ('b', 2), ('c', 3)})
    True
    >>> is_injective({('a', 1), ('b', 2), ('c', 1)})
    False
    """
    # : implement
    outputs = [y for x, y in pairs]
    return len(outputs) == len(set(outputs))


def is_surjective(pairs: set, codomain: set) -> bool:
    """Return whether the function given by pairs hits every codomain element.

    >>> is_surjective({('a', 1), ('b', 2), ('c', 3)}, {1, 2, 3})
    True
    >>> is_surjective({('a', 1), ('b', 2), ('c', 1)}, {1, 2, 3})
    False
    """
    # : implement
    outputs = {y for x, y in pairs}
    return codomain.issubset(outputs)


F_PAIRS = {('a', 1), ('b', 2), ('c', 1)}
F_CODOMAIN = {1, 2, 3}

# : (c) store checker results for F
f_is_injective = is_injective(F_PAIRS)   # False
f_is_surjective = is_surjective(F_PAIRS, F_CODOMAIN)  # False


# =============================================================================
# Q5: Capstone — testing the Wordle scorer
# =============================================================================
# Q5 TEST PLAN: (one short phrase per test naming the behaviour it targets)
# : test_score_guess_all_correct -> all exact matches
# : test_score_guess_all_incorrect -> no shared letters
# : test_score_guess_out_of_place -> misplaced letters
# : test_score_guess_duplicate_letter -> duplicate overclaim
# : test_naive_differs_from_correct_on_duplicates -> naive scorer regression


def test_score_guess_all_correct():
    """Guess equals secret -> every position Correct."""
    assert score_guess('crane', 'crane') == ['Correct', 'Correct', 'Correct', 'Correct', 'Correct']


def test_score_guess_all_incorrect():
    """No shared letters -> every position Incorrect."""
    assert score_guess('mmmmm', 'crane') == ['Incorrect', 'Incorrect', 'Incorrect', 'Incorrect', 'Incorrect']


def test_score_guess_out_of_place():
    """At least one Out of place; avoid duplicate-letter complications."""
    assert score_guess('range', 'crane') == ['Out of place', 'Out of place', 'Out of place', 'Incorrect', 'Correct']


def test_score_guess_duplicate_letter():
    """Guess repeats a letter more times than secret contains it."""
    assert score_guess('pappa', 'apple') == ['Out of place', 'Out of place', 'Correct', 'Incorrect', 'Incorrect']


def test_naive_differs_from_correct_on_duplicates():
    """Document that naive_score_guess disagrees on a duplicate case."""
    assert naive_score_guess('pappa', 'apple') != score_guess('pappa', 'apple')


if __name__ == '__main__':
    print('Q2 is_valid_guess:', is_valid_guess('crane', 5))
    print('Q2 score_guess crane/crane:', score_guess('crane', 'crane'))
    print('Q2 score_guess aaaaa/crane:', score_guess('aaaaa', 'crane'))
    print('Q3 is_valid_guess_fixed:', is_valid_guess_fixed('crane', 5))
    print('Q3 guesses_remaining_fixed:', guesses_remaining_fixed(2))
    print('Q3 naive pappa/apple:', naive_score_guess('pappa', 'apple'))
    print('Q3 format_guess_number_fixed:', format_guess_number_fixed(3))
    print('Q4 injective:', is_injective(F_PAIRS))
    print('Q4 surjective:', is_surjective(F_PAIRS, F_CODOMAIN))
    print('Q4 flags:', f_is_injective, f_is_surjective)

    # Run the student-authored Q5 tests (plain asserts).
    for _test in (
        test_score_guess_all_correct,
        test_score_guess_all_incorrect,
        test_score_guess_out_of_place,
        test_score_guess_duplicate_letter,
        test_naive_differs_from_correct_on_duplicates,
    ):
        _test()
        print('Q5', _test.__name__, 'OK')
