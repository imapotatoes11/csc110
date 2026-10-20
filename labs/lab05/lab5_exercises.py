"""CSC110 Lab 5: Exercises (Week 5 Review)

Complete the TODOs below, in order. See the lab handout for full instructions.

WARNING: Do not modify the comments or variable names in this file except to fill
in the requested answers and to remove a TODO once you have finished a task.
Automated marking scripts will look for these exact names.
"""

# =============================================================================
# Q1: Tracing dictionaries, sets, and tuples by hand
# =============================================================================
# : predicted print(inventory['pens']) -> 12
# : predicted print('markers' in inventory) -> False
# : predicted print(inventory.get('markers', 0)) -> 0
# : predicted print(sorted(both)) -> ['Bob']
# : predicted print(sorted(only_utm)) -> ['Alice', 'Carol']
# : predicted print(pair in edges) -> False
# : predicted print(total) in Snippet C -> 2


def snippet_a() -> tuple[int, bool, int]:
    """Run Snippet A from the handout and return
    (inventory['pens'], 'markers' in inventory, inventory.get('markers', 0)).

    >>> snippet_a()
    (12, False, 0)
    """
    inventory = {'pens': 12, 'notebooks': 4}
    inventory['erasers'] = 6
    return inventory['pens'], 'markers' in inventory, inventory.get('markers', 0)


def snippet_b() -> tuple[list[str], list[str], bool]:
    """Run Snippet B from the handout and return
    (sorted(both), sorted(only_utm), pair in edges).

    >>> snippet_b()
    (['Bob'], ['Alice', 'Carol'], False)
    """
    utm = {'Alice', 'Bob', 'Carol'}
    utsg = {'Bob', 'Dave'}
    both = utm & utsg
    only_utm = utm - utsg
    pair = ('Bob', 'Dave')
    edges = {('Alice', 'Bob'), ('Bob', 'Carol')}
    return sorted(both), sorted(only_utm), pair in edges


def snippet_c() -> int:
    """Run Snippet C from the handout and return `total`.

    >>> snippet_c()
    2
    """
    grades = {'Alice': 91, 'Bob': 78, 'Carol': 85}
    total = 0
    for name, score in grades.items():
        if score >= 80:
            total = total + 1
    return total


# =============================================================================
# Q2: Building and using dictionaries
# =============================================================================

def build_appointment_counts(names: list[str], counts: list[int]) -> dict[str, int]:
    """Return a dict mapping each name to its matching appointment count.

    Precondition: len(names) == len(counts); names are unique.

    >>> build_appointment_counts(['Ada', 'Grace'], [3, 1])
    {'Ada': 3, 'Grace': 1}
    """
    # : implement
    return {i: j for i,j in zip(names, counts)}


def students_with_at_least(appointments: dict[str, int], threshold: int) -> list[str]:
    """Return alphabetically sorted names whose count is >= threshold.

    >>> students_with_at_least({'Ada': 3, 'Grace': 1, 'Barbara': 3}, 3)
    ['Ada', 'Barbara']
    >>> students_with_at_least({'Ada': 1}, 5)
    []
    """
    # : implement
    return sorted([i for i,j in appointments.items() if j >= threshold])


def letter_frequencies(word: str) -> dict[str, int]:
    """Return a frequency map of each distinct character in word.

    >>> letter_frequencies('crane')
    {'c': 1, 'r': 1, 'a': 1, 'n': 1, 'e': 1}
    >>> letter_frequencies('apple')
    {'a': 1, 'p': 2, 'l': 1, 'e': 1}
    >>> letter_frequencies('')
    {}
    """
    # : implement
    out = {}
    for char in word:
        out[char] = out.get(char, 0) + 1
    return out


# =============================================================================
# Q3: Debugging & reasoning
# =============================================================================

# --- Item 1: KeyError ---
# : what happens when item is missing from inventory in the buggy version?
# The function throws a KeyError when an item is not in the inventory.

def get_stock(inventory: dict, item: str) -> int:
    """Return how many of `item` are in stock. Missing items count as 0.

    >>> get_stock({'pens': 12}, 'pens')
    12
    >>> get_stock({'pens': 12}, 'markers')
    0
    """
    # : write a corrected version that does not raise KeyError.
    return inventory.get(item, 0)


# --- Item 2: enumerate mix-up ---
# : what does `for name, score in enumerate(grades):` actually bind to
# name and score? Rewrite the correct loop as a comment under this TODO.
# In the given snippet, `enumerate(grades)` assigns the index of the key to `name`, and the key to `score`.
# The correct loop should be `for name, score in grades.items():`


# --- Item 3: symmetry check that isn't ---
# : why does the buggy is_symmetric always return True if it finishes?
# : what should each pair (a, b) be checked against instead?
# The buggy code essentially checks if every pair (that is inside the relation) exists inside the relation, which is always true.
# Each pair `(a, b)` should instead be checked against `(b, a)` to correctly check symmetry.


# --- Item 4: set/list confusion ---
# : why is the classmate's fix a bad idea?
# A list can have duplicates (unlike a set); allowing duplicates would not return unique values.


# =============================================================================
# Q4: Equivalence relations — proof and counterexample, then code
# =============================================================================
# Part (a): fill-in blanks for the "same remainder mod 3" proof
# : (1) a
# : (2) the same
# : (3) r
# : (4) equivalence relation
#
# Part (b): A_EXAMPLE / R_EXAMPLE below
# : reflexive? True
# : symmetric? True
# : transitive? False: 1 ~ 2 ^ 2 ~ 3, but 1 !~ 3  (if not, give a counterexample)


def is_reflexive(A: set, R: set) -> bool:
    """Return whether R is a reflexive relation on A.

    >>> is_reflexive({1, 2}, {(1, 1), (2, 2), (1, 2)})
    True
    >>> is_reflexive({1, 2}, {(1, 1)})
    False
    """
    # : implement
    for i in A:
        if (i, i) not in R:
            return False
    return True


def is_symmetric(A: set, R: set) -> bool:
    """Return whether R is a symmetric relation on A.

    (Pairs whose endpoints are outside A can be ignored for this lab.)

    >>> is_symmetric({1, 2}, {(1, 2), (2, 1), (1, 1), (2, 2)})
    True
    >>> is_symmetric({1, 2}, {(1, 2), (1, 1), (2, 2)})
    False
    """
    # : implement
    for a in A:
        for b in A:
            if (a, b) in R and (b, a) not in R:
                return False
    return True


def is_transitive(A: set, R: set) -> bool:
    """Return whether R is a transitive relation on A.

    >>> is_transitive({1, 2, 3}, {(1, 2), (2, 3), (1, 3), (1, 1), (2, 2), (3, 3)})
    True
    >>> is_transitive({1, 2, 3}, {(1, 2), (2, 3), (1, 1), (2, 2), (3, 3)})
    False
    """
    # : implement
    for a in A:
        for b in A:
            for c in A:
                if (a, b) in R and (b, c) in R:
                    if (a, c) not in R:
                        return False
    return True


# Part (c).1: finite piece of the mod-3 relation from part (a)
A_MOD = {0, 1, 2, 3, 4, 5}
R_MOD = {(a, b) for a in A_MOD for b in A_MOD if a % 3 == b % 3} # build all (a, b) in A_MOD x A_MOD with a % 3 == b % 3

mod_is_reflexive = is_reflexive(A_MOD, R_MOD)   # True
mod_is_symmetric = is_symmetric(A_MOD, R_MOD)   # True
mod_is_transitive = is_transitive(A_MOD, R_MOD)  # True

# Part (c).2: the finite counterexample from part (b)
A_EXAMPLE = {1, 2, 3}
R_EXAMPLE = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1), (2, 3), (3, 2)}

r_is_reflexive = is_reflexive(A_EXAMPLE, R_EXAMPLE)   # True
r_is_symmetric = is_symmetric(A_EXAMPLE, R_EXAMPLE)   # True
r_is_transitive = is_transitive(A_EXAMPLE, R_EXAMPLE)  # False


# =============================================================================
# Q5: Capstone — equivalence classes via dictionaries
# =============================================================================
# : in 1-2 sentences, why is "same length" an equivalence relation?
# "same length" satisfies all of reflexivity, symmetry, and transitivity:
# reflexive: every word has the same length as itself
# symmetric: if u and v have the same length, then v and u have the same length
# transitive: if u and v have the same length and v and w have the same length, then u and w have the same length.
# Since "same length" satisfies all three properties, it is an equivalence relation.

def group_by_length(words: list[str]) -> dict[int, list[str]]:
    """Group words by length; preserve first-seen order within each group.

    >>> group_by_length(['to', 'be', 'or', 'not', 'to', 'be'])
    {2: ['to', 'be', 'or'], 3: ['not']}
    >>> group_by_length([])
    {}
    """
    # : implement
    result = {}

    for word in words:
        length = len(word)
        if length not in result:
            result[length] = []
        if word not in result[length]:
            result[length].append(word)
    return result


def same_length_pairs(words: list[str]) -> set[tuple[str, str]]:
    """Return ordered pairs (u, v) of distinct-word elements with equal length.

    Includes reflexive pairs (w, w). Duplicate strings in `words` are treated
    as a single element.

    >>> sorted(same_length_pairs(['to', 'be', 'not']))
    [('be', 'be'), ('be', 'to'), ('not', 'not'), ('to', 'be'), ('to', 'to')]
    """
    # : implement
    out = set()
    unique_words = set(words)
    for i in unique_words:
        for j in unique_words:
            if len(i) == len(j):
                out.add((i, j))
    return out


if __name__ == '__main__':
    print('Q1 snippet_a():', snippet_a())
    print('Q1 snippet_b():', snippet_b())
    print('Q1 snippet_c():', snippet_c())
    print('Q2 build:', build_appointment_counts(['Ada', 'Grace'], [3, 1]))
    print('Q2 at_least:', students_with_at_least({'Ada': 3, 'Grace': 1, 'Barbara': 3}, 3))
    print('Q2 freqs:', letter_frequencies('apple'))
    print('Q3 get_stock:', get_stock({'pens': 12}, 'markers'))
    print('Q4 mod flags:', mod_is_reflexive, mod_is_symmetric, mod_is_transitive)
    print('Q4 r flags:', r_is_reflexive, r_is_symmetric, r_is_transitive)
    print('Q4 R_MOD size:', len(R_MOD))

    print('Q5 groups:', group_by_length(['to', 'be', 'or', 'not', 'to', 'be']))
    print('Q5 pairs:', sorted(same_length_pairs(['to', 'be', 'not'])))
