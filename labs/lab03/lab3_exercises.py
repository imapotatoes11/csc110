"""CSC110 Lab 3: Exercises (Week 3 Review)

Complete the TODOs below, in order. See the lab handout for full instructions.

WARNING: Do not modify the comments or variable names in this file.
Automated marking scripts will look for these exact names.

Exercises 2 and 5 are PROBE-ABLE PROBLEMS -- see the handout's "A new kind of
exercise this week" section before starting them. To solve them, visit:

https://quickta.utm.utoronto.ca/?view=probeable-problem-set

And then select the "W4 Probeable Problems" Deployment. There should be 3 
problems to complete, 1 for exercise 2 and 2 for exercise 5.
"""

# =============================================================================
# Q1: Tracing loop code by hand
# =============================================================================
# : predicted value of total in Snippet A (while i <= 5) -> 15
# : predicted value of total in Snippet A's variant (while i < 5)  -> 10. this one skips over i=5, resulting in 5 less than the expected.
# : predicted value of total in Snippet B (threshold counting) -> 3

def snippet_a(limit: int, use_lt: bool) -> int:
    """Run Snippet A from the handout. If use_lt is False, use the condition
    `i <= limit` (as originally shown); if True, use `i < limit` instead.

    >>> snippet_a(5, False)
    15
    >>> snippet_a(5, True)
    10
    """
    total = 0
    i = 1
    if not use_lt:
        while i <= limit:
            total = total + i
            i = i + 1
    else:
        while i < limit:
            total = total + i
            i = i + 1
    return total


def snippet_b_by_index(scores: list[int]) -> int:
    """Run Snippet B from the handout (indexing version): count how many
    scores are >= 70.

    >>> snippet_b_by_index([70, 85, 60, 95])
    3
    """
    total = 0
    for i in range(len(scores)):
        if scores[i] >= 70:
            total = total + 1
    return total


def snippet_b_by_value(scores: list[int]) -> int:
    """Same as snippet_b_by_index, but iterating directly over the values
    instead of indices (the 'two ways to iterate' idea from Module 3.2).
    Should always agree with snippet_b_by_index for the same input.

    complete this function, and use a different loop than by_index
    """
    total = 0
    for score in scores:
        total += score >= 70
    return total


# =============================================================================
# Q2 -- PROBE-ABLE: Event ticket code validator
# =============================================================================
# TODO Q2 SPEC NOTES: (write at least 3 specific facts you learned from
# probing the spec and roughly what question got you each one)
#  1. every valid code has exactly 3 UPPERCASE letters, followed by 5 digits: 4 ticket-number digits and one check digit. no separators
#  2. letters are uppercase A-Z. digit chars are unaffected by caps
#  3.valid codes cannot start with a number
#  4. venue portion is case-sensitive: lowercase is invalid
#  5. spaces are not allowed
#  6. ticket-number digits: positions 4-7
#  7. check digit: position 8, exactly one digit calculated as follows:
#    - sum of ticket-number digits mod 10.

def is_valid_ticket_code(code: str) -> bool:
    """Return whether code is a valid event ticket code.

    You must probe the spec before you'll know the exact rules. 
    """
    # : implement per the probed specification.
    if len(code) != 8:
        return False
    letters, digits = code[:3], code[3:]
    if not all('A' <= c <= 'Z' for c in letters):
        return False
    if not all(c in '0123456789' for c in digits):
        return False
    return sum(int(c) for c in digits[:4]) % 10 == int(digits[4])


# =============================================================================
# Q3: Debugging & reasoning practice
# =============================================================================
# For items 1-2, write a CORRECTED version of the function (don't just
# describe the fix in a comment -- the corrected function must actually run).

# --- Item 1: infinite loop ---
# : what's missing from the buggy sum_up_to, and why does it loop forever?
# The index does not increment, so if `i<=n`, then `i` will always be greater than or equal to `n`.

def sum_up_to_fixed(n: int) -> int:
    """Return 1 + 2 + ... + n. 

    >>> sum_up_to_fixed(5)
    15
    """
    # : write a corrected version here.
    total = 0
    i = 1
    while i <= n:
        total = total + i
        i += 1
    return total


# --- Item 2: off-by-one for loop ---
# : what does the buggy count_evens([2, 4, 6, 8]) actually return, and
# what SHOULD it return?
# The exmaple code does not consider the last element in the list.
# So in the case of [2,4,6,8], the loop will stop before 8, and return a count
# of 3 (it should return 4).

def count_evens_fixed(numbers: list[int]) -> int:
    """Return how many numbers in the list are even. 

    >>> count_evens_fixed([2, 4, 6, 8])
    4
    """
    # : write a corrected version here.
    count = 0
    for i in numbers:
        if i % 2 == 0:
            count += 1
    return count


# --- Item 3: quantifier mistranslation ---
# : is the student's forall-translation correct? Using 2 and 3 (both
# prime), show the student's version and the correct version disagree, and
# write the CORRECT translation (in words or symbols) as a comment.
# The student's translation is incorrect.
# The correct version should show that 2 is an even prime, but 3 is not an even prime.
# The student's claim explains that EVERY prime number is even, which it is not (3 is a counterexample)
# The correct claim should be: "There exists x in Primes such that x is even".

# --- Item 4: quantifier-order bug in code ---
# : in words, what claim does `any(all(likes(p, f) for p in people) for
# f in foods)` actually check? Then write the CORRECTED version (as a comment
# containing the corrected expression) that checks "everyone in people likes
# something in foods".
# The given code checks if there is at least one food that EVERYONE likes.
# Corrected: all(any(likes(p, f) for f in foods) for p in people)


# =============================================================================
# Q4: Translating and evaluating quantified statements
# =============================================================================
# D = {2, 3, 4, 5, 6}
# : (a) translate "there is a number in D that is prime, and one more
# than it is also prime" using exists; true or false? if true, give a witness:
# ∃x∈D s.t. x is prime ∧ x+1 is prime
# The statment is true. D=2 is prime and D=3 is the subsequent element and is also prime.
# : (b) translate "every even number in D has an even square" using
# forall; true or false? 
# ∀x∈D, (x mod 2) = 0 -> (x^2 mod 2) = 0
# This statement is true.

def likes(a: str, b: str) -> bool:
    """Return whether a likes b, for the People = ['Alice', 'Bob', 'Carol']
    cycle from the handout: Alice likes Bob, Bob likes Carol, Carol likes
    Alice, and no one likes anyone else (including themselves).

    >>> likes('Alice', 'Bob')
    True
    >>> likes('Bob', 'Alice')
    False
    """
    # : implement using the pairs given in the handout.
    return any([(a,b) == (i,j) for i,j in [("Alice", "Bob"), ("Bob", "Carol"), ("Carol", "Alice")]])


# : (c) using any/all and the `likes` function above, compute whether
# "forall a exists b, likes(a, b)" is true (store your answer in
# everyone_likes_someone below)
People = ['Alice', 'Bob', 'Carol']
everyone_likes_someone = all(any(likes(a, b) for b in People) for a in People)  # True

# : (d) similarly, compute whether "exists b forall a, likes(a, b)" is
# true (store your answer in someone_liked_by_everyone below)
someone_liked_by_everyone = any(all(likes(a, b) for a in People) for b in People) # False

# : (e) in a comment, explain in 1-2 sentences why (c) and (d) disagree.
# for (c), there can be a different b for every a, meaning someone (not necessarily
# the same person) likes someone else. for (d), there has to be a common person that
# everyone likes, which is false.


# =============================================================================
# Q5 -- PROBE-ABLE: Formalize and verify a roster claim
# =============================================================================
#  Q5 SPEC NOTES: (write at least 3 specific facts you learned from
# probing the spec and roughly what question got you each one)
#  1. roster is in the following format:
#  roster = [
#     {'name': 'Ava', 'lab2_submitted': True, 'overall_grade': 82},
#     {'name': 'Ben', 'lab2_submitted': False, 'overall_grade': 40}
# ]
#  2. Should return `True` if the roster is empty.
#  3. Should return `True` if no students have submitted lab 2

# : (a) write the claim using quantifier notation (forall/implication)
# over the appropriate domain, as a comment.
# "Every student who submitted Lab 2 also has a passing overall grade"
# ∀x ∈ (All students), submitted_lab_2(x) => overall_grade(x) >= 50

def check_roster_claim(roster: list[dict]) -> bool:
    """You must probe the spec before you'll know the exact rules.
    """
    # : implement per the probed specification.
    return all([(not i['lab2_submitted']) or (i['lab2_submitted'] and i['overall_grade'] >= 50) for i in roster])


def find_counterexample(roster: list[dict]) -> str | None:
    """You must probe the spec before you'll know the exact rules.
    """
    # : implement per the probed specification.
    for i in roster:
        if i['lab2_submitted'] and i['overall_grade'] < 50:
            return i['name']
    return None




if __name__ == '__main__':
    print('Q1 snippet_a(5, False):', snippet_a(5, False))
    print('Q1 snippet_b_by_index:', snippet_b_by_index([70, 85, 60, 95]))
    print('Q1 snippet_b_by_value:', snippet_b_by_value([70, 85, 60, 95]))
    print('Q3 sum_up_to_fixed(5):', sum_up_to_fixed(5))
    print('Q3 count_evens_fixed([2, 4, 6, 8]):', count_evens_fixed([2, 4, 6, 8]))
    print('Q4 likes("Alice", "Bob"):', likes('Alice', 'Bob'))
