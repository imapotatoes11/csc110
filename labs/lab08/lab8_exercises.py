"""CSC110 Lab 8: Exercises (Week 8 Review)

Complete the TODOs below, in order. See the lab handout for full instructions.

WARNING: Do not modify the comments or variable names in this file except to fill
in the requested answers and to remove a TODO once you have finished a task.
Automated marking scripts will look for these exact names.

Exercise 5 is a PROBE-ABLE PROBLEM. Visit:
https://quickta.utm.utoronto.ca/?view=probeable-problem-set
and select the "W9" Deployment.
"""

# =============================================================================
# Q1: Tracing identity, mutation, and aliasing by hand
# =============================================================================
# : predicted print(grades) -> [['Ada', 85], ['Grace', 90], ['Lin', 70]]
# : predicted print(alias) -> [['Ada', 85], ['Grace', 90], ['Lin', 70]]
# : predicted print(shallow) -> [['Ada', 85], ['Grace', 90]]
# : predicted print(deep) -> [['Ada', 80], ['Grace', 95]]
# : why did shallow[0][1] = 85 change grades, while deep[1][1] = 95 did not?
# shallow shares the inner lists with grades, whereas deep containes
#   actual copies of said inner lists
# : predicted print(x == y) -> True
# : predicted print(x is y) -> False
# : predicted print(x is z) -> True
# : predicted print(x[0] is y[0]) -> False
# : predicted print(x[0] is z[0]) -> True


def snippet_a() -> tuple[list, list, list, list]:
    """Run Snippet A (including its prints). Return (grades, alias, shallow, deep).

    >>> snippet_a()
    [['Ada', 85], ['Grace', 90], ['Lin', 70]]
    [['Ada', 85], ['Grace', 90], ['Lin', 70]]
    [['Ada', 85], ['Grace', 90]]
    [['Ada', 80], ['Grace', 95]]
    ([['Ada', 85], ['Grace', 90], ['Lin', 70]], [['Ada', 85], ['Grace', 90], ['Lin', 70]], [['Ada', 85], ['Grace', 90]], [['Ada', 80], ['Grace', 95]])
    """
    grades = [['Ada', 80], ['Grace', 90]]
    alias = grades
    shallow = grades[:]
    deep = [row[:] for row in grades]

    alias.append(['Lin', 70])
    shallow[0][1] = 85
    deep[1][1] = 95

    print(grades)
    print(alias)
    print(shallow)
    print(deep)
    return grades, alias, shallow, deep


def snippet_b() -> tuple[bool, bool, bool, bool, bool]:
    """Run Snippet B (including its prints).

    Return (x == y, x is y, x is z, x[0] is y[0], x[0] is z[0]).

    >>> snippet_b()
    True
    False
    True
    False
    True
    (True, False, True, False, True)
    """
    x = [[10], [20]]
    y = [[10], [20]]
    z = x
    print(x == y)
    print(x is y)
    print(x is z)
    print(x[0] is y[0])
    print(x[0] is z[0])
    return x == y, x is y, x is z, x[0] is y[0], x[0] is z[0]


# =============================================================================
# Q2: Writing memory-safe helpers
# =============================================================================

def copy_score_rows(rows: list[list[int]]) -> list[list[int]]:
    """Return a deep copy of a list of lists of integers.

    The result is a new outer list, and each row is a new inner list.
    Do not use the copy module.

    >>> original = [[80, 90], [70]]
    >>> copied = copy_score_rows(original)
    >>> copied[0][0] = 0
    >>> original
    [[80, 90], [70]]
    >>> copied.append([1])
    >>> original
    [[80, 90], [70]]
    """
    # : implement
    return [[j for j in i] for i in rows]


def append_unique(values: list[str], item: str) -> None:
    """Append item to values if it is not already present. Mutates values.

    >>> words = ['a', 'b']
    >>> append_unique(words, 'c')
    >>> words
    ['a', 'b', 'c']
    >>> append_unique(words, 'a')
    >>> words
    ['a', 'b', 'c']
    """
    # : implement
    if item not in values:
        values.append(item)


def shared_identity(a: list, b: list) -> bool:
    """Return whether a and b are the same list object.

    >>> xs = [1]
    >>> shared_identity(xs, xs)
    True
    >>> shared_identity(xs, [1])
    False
    """
    # : implement
    return a is b


# =============================================================================
# Q3: Debugging & reasoning
# =============================================================================

# --- Item 1: aliasing bug ---
# : after the buggy top_two on a 3+ element list, is (scores is result)
# True or False, and why?
# False. result is a slice of scores (scores[:2]), creating a new list object (that isn't scores)

def top_two_fixed(scores: list[int]) -> list[int]:
    """Return the two highest scores without disturbing the caller's list.

    >>> nums = [55, 88, 42, 91, 67]
    >>> top_two_fixed(nums)
    [91, 88]
    >>> nums
    [55, 88, 42, 91, 67]
    """
    # : implement
    return sorted(scores, reverse=True)[:2]


# --- Item 2: traceback reading ---
# : which frame raised? which function called that frame?
# The exception was raised in print_report on line 8
# print_report was called by the global frame at line 12.

# --- Item 3: immutable rebinding ---
# : predicted print(s) -> 'crane!'
# : predicted print(t) -> 'crane'
# : one-sentence explanation: strings are immutable, so the line `s = s + '!'` created a new string object


# =============================================================================
# Q4: Contrapositive fill-in (+ contradiction warm-up)
# =============================================================================
# : (1) x < 5 and y < 5
# : (2) x < 5 and y < 5
# : (3) x + y < 10
# : contradiction assumption ¬S for "no smallest positive real":
# Assume that there exists a positive real number n such that for all positive real numbers x, n <= x


# =============================================================================
# Q5 -- PROBE-ABLE: apply grade updates
# =============================================================================
# TODO Q5 SPEC NOTES: (write at least 3 specific facts you learned from probing)
#  1. roster has student name as key
#  2. the value of roster is a list of the student's scores
#  3. skip names in updates that aren't on the roster

def apply_updates(roster: dict, updates: list) -> dict:
    """Apply grade updates to a roster.

    You must probe the spec before you'll know the exact rules.
    """
    # : implement per the probed specification.
    from copy import deepcopy
    roster = deepcopy(roster)
    for update in updates:
        name = update[0]
        if name in roster:
            scores = roster[name]
            if 0 <= update[1] < len(scores):
                scores[update[1]] = update[2]
    return roster


if __name__ == '__main__':
    print('Q1 Snippet A:')
    snippet_a()
    print('Q1 Snippet B:')
    snippet_b()
    print('Q2 copy_score_rows:', copy_score_rows([[80, 90], [70]]))
    print('Q2 shared_identity:', shared_identity([1], [1]))
