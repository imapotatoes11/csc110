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
# TODO: predicted value of total in Snippet A (while i <= 5) -> 15
# TODO: predicted value of total in Snippet A's variant (while i < 5)  -> 10
# TODO: predicted value of total in Snippet B (threshold counting) -> 3

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

    TODO: complete this function, and use a different loop than by_index
    """


# =============================================================================
# Q2 -- PROBE-ABLE: Event ticket code validator
# =============================================================================
# TODO Q2 SPEC NOTES: (write at least 3 specific facts you learned from
# probing the spec and roughly what question got you each one)
#  1.
#  2.
#  3.

def is_valid_ticket_code(code: str) -> bool:
    """Return whether code is a valid event ticket code.

    You must probe the spec before you'll know the exact rules. 
    """
    # TODO: implement per the probed specification.


# =============================================================================
# Q3: Debugging & reasoning practice
# =============================================================================
# For items 1-2, write a CORRECTED version of the function (don't just
# describe the fix in a comment -- the corrected function must actually run).

# --- Item 1: infinite loop ---
# TODO: what's missing from the buggy sum_up_to, and why does it loop forever?

def sum_up_to_fixed(n: int) -> int:
    """Return 1 + 2 + ... + n. 

    >>> sum_up_to_fixed(5)
    15
    """
    # TODO: write a corrected version here.


# --- Item 2: off-by-one for loop ---
# TODO: what does the buggy count_evens([2, 4, 6, 8]) actually return, and
# what SHOULD it return?

def count_evens_fixed(numbers: list[int]) -> int:
    """Return how many numbers in the list are even. 

    >>> count_evens_fixed([2, 4, 6, 8])
    4
    """
    # TODO: write a corrected version here.


# --- Item 3: quantifier mistranslation ---
# TODO: is the student's forall-translation correct? Using 2 and 3 (both
# prime), show the student's version and the correct version disagree, and
# write the CORRECT translation (in words or symbols) as a comment.

# --- Item 4: quantifier-order bug in code ---
# TODO: in words, what claim does `any(all(likes(p, f) for p in people) for
# f in foods)` actually check? Then write the CORRECTED version (as a comment
# containing the corrected expression) that checks "everyone in people likes
# something in foods".


# =============================================================================
# Q4: Translating and evaluating quantified statements
# =============================================================================
# D = {2, 3, 4, 5, 6}
# TODO: (a) translate "there is a number in D that is prime, and one more
# than it is also prime" using exists; true or false? if true, give a witness:
# TODO: (b) translate "every even number in D has an even square" using
# forall; true or false? 

def likes(a: str, b: str) -> bool:
    """Return whether a likes b, for the People = ['Alice', 'Bob', 'Carol']
    cycle from the handout: Alice likes Bob, Bob likes Carol, Carol likes
    Alice, and no one likes anyone else (including themselves).

    >>> likes('Alice', 'Bob')
    True
    >>> likes('Bob', 'Alice')
    False
    """
    # TODO: implement using the pairs given in the handout.


# TODO: (c) using any/all and the `likes` function above, compute whether
# "forall a exists b, likes(a, b)" is true (store your answer in
# everyone_likes_someone below)
People = ['Alice', 'Bob', 'Carol']
everyone_likes_someone = None  # TODO

# TODO: (d) similarly, compute whether "exists b forall a, likes(a, b)" is
# true (store your answer in someone_liked_by_everyone below)
someone_liked_by_everyone = None  # TODO

# TODO: (e) in a comment, explain in 1-2 sentences why (c) and (d) disagree.


# =============================================================================
# Q5 -- PROBE-ABLE: Formalize and verify a roster claim
# =============================================================================
# TODO Q5 SPEC NOTES: (write at least 3 specific facts you learned from
# probing the spec and roughly what question got you each one)
#  1.
#  2.
#  3.

# TODO: (a) write the claim using quantifier notation (forall/implication)
# over the appropriate domain, as a comment.

def check_roster_claim(roster: list[dict]) -> bool:
    """You must probe the spec before you'll know the exact rules.
    """
    # TODO: implement per the probed specification.


def find_counterexample(roster: list[dict]) -> str | None:
    """You must probe the spec before you'll know the exact rules.
    """
    # TODO: implement per the probed specification.


# TODO: (d) after implementing, in a comment: is the claim true or false for
# sample_roster? if false, who's the counterexample?


if __name__ == '__main__':
    print('Q1 snippet_a(5, False):', snippet_a(5, False))
    print('Q1 snippet_b_by_index:', snippet_b_by_index([70, 85, 60, 95]))
    print('Q1 snippet_b_by_value:', snippet_b_by_value([70, 85, 60, 95]))
    print('Q3 sum_up_to_fixed(5):', sum_up_to_fixed(5))
    print('Q3 count_evens_fixed([2, 4, 6, 8]):', count_evens_fixed([2, 4, 6, 8]))
    print('Q4 likes("Alice", "Bob"):', likes('Alice', 'Bob'))
