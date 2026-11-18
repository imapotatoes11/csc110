"""CSC110 Lab 7: Exercises (Week 7 Review)

Complete the TODOs below, in order. See the lab handout for full instructions.

WARNING: Do not modify the comments or variable names in this file except to fill
in the requested answers and to remove a TODO once you have finished a task.
Automated marking scripts will look for these exact names.

Exercise 2 is a PROBE-ABLE PROBLEM. Visit:
https://quickta.utm.utoronto.ca/?view=probeable-problem-set
and select the "W8 Probeable Problems" Deployment.
"""

# =============================================================================
# Q1: Tracing exceptions and CSV parsing by hand
# =============================================================================
# : predicted print(safe_int('42')) -> 42
# : predicted print(safe_int('4.2')) -> None
# : predicted print(safe_int('crane')) -> None
# : predicted print(parts) -> ['Ada','90','True']
# : predicted print(parts[1]) -> '90'
# : predicted print(int(parts[1]) + 5) -> 95


def safe_int(text: str) -> int | None:
    """Return int(text), or None if text is not a valid integer literal."""
    try:
        return int(text)
    except ValueError:
        return None


def snippet_a() -> tuple[int | None, int | None, int | None]:
    """Run Snippet A (including its prints). Return the three safe_int results.

    >>> snippet_a()
    42
    None
    None
    (42, None, None)
    """
    r1 = safe_int('42')
    r2 = safe_int('4.2')
    r3 = safe_int('crane')
    print(r1)
    print(r2)
    print(r3)
    return r1, r2, r3


def snippet_b() -> tuple[list[str], str, int]:
    """Run Snippet B (including its prints). Return (parts, parts[1], int+5).

    >>> snippet_b()
    ['Ada', '90', 'True']
    90
    95
    (['Ada', '90', 'True'], '90', 95)
    """
    line = 'Ada,90,True'
    parts = line.strip().split(',')
    print(parts)
    print(parts[1])
    print(int(parts[1]) + 5)
    return parts, parts[1], int(parts[1]) + 5


# =============================================================================
# Q2 -- PROBE-ABLE: Lab attendance CSV summary
# =============================================================================
#  Q2 SPEC NOTES: (write at least 3 specific facts you learned from probing)
#  1. File has columns `utorid,status`
#  2. status is either `P` or `A` (e.g. `a` or `p` will not appear)
#  3. utorid is case sensitive (?) 

from typing import TextIO
def summarize_attendance(f: TextIO) -> dict:
    """Return present/absent counts for a lab attendance CSV.

    You must probe the spec before you'll know the exact rules.
    """
    # : implement per the probed specification.
    out = {"present": 0, "absent": 0}
    seen = set()

    for line in f.read().splitlines()[1:]:
        fields = line.split(",")

        if len(fields) != 2:
            continue

        utorid, status = fields
        utorid = utorid.strip()
        status = status.strip()

        if status not in ("P", "A"):
            continue

        if utorid in seen:
            continue

        seen.add(utorid)
        out["present" if status == "P" else "absent"] += 1

    return out



# =============================================================================
# Q3: Debugging & reasoning
# =============================================================================

# --- Item 1: bare except ---
# : which exception(s) should be caught instead of a bare except?
# OSError should be caught.

def load_first_line_fixed(path: str) -> str:
    """Return the first line of the file, or '' if it can't be opened.

    >>> # Behaviour checked by the TA suite with temporary files.
    """
    # : implement
    try:
        with open(path) as f:
            return f.readline()
    except OSError:
        return ''


# --- Item 2: forgetting the CSV header ---
# : what goes wrong when the first line is 'name,score'?
# The first (header) line `name,score` throws a ValueError when trying to convert 'score' to an int.

def sum_scores_fixed(path: str) -> int:
    """Sum the score column of a name,score CSV.

    >>> # Behaviour checked by the TA suite with temporary files.
    """
    # : implement
    total = 0
    with open(path) as f:
        f.readline()
        for line in f:
            name, score = line.strip().split(',')
            total = total + int(score)
    return total


# --- Item 3: testing-domain miss ---
# : name one missed edge-case category and one concrete input for safe_int:
# The tests miss when the input is a negative number. e.g. `safe_int('-5')`


# =============================================================================
# Q4: Direct proof — product of two odds is odd
# =============================================================================
# : (1) a = 2p + 1 and b = 2q + 1
# : (2) 2pq + p + q
# : (3) the definition of odd


def is_odd(n: int) -> bool:
    """Return whether n is odd.

    >>> is_odd(3)
    True
    >>> is_odd(4)
    False
    """
    # : implement
    return n % 2 == 1


def product_of_odds_is_odd(n: int) -> bool:
    """Return whether all pairs of odd numbers a and b, 0 < a <= b <= n produce 
    an odd product.

    >>> product_of_odds_is_odd(15)
    True
    """
    # : implement
    for i in range(1, n + 1, 2):
        for j in range(i, n + 1, 2):
            if not is_odd(i * j):
                return False
    return True


# =============================================================================
# Q5: Capstone — average a CSV column
# =============================================================================

def average_score(path: str) -> float:
    """Return the average of the score column in a name,score CSV with a header.

    Raise ValueError if there are no data rows after the header.
    Do not catch file-open errors.

    >>> # Behaviour checked by the TA suite with temporary files.
    """
    # : implement
    total, count = 0, 0
    with open(path) as f:
        f.readline()
        for line in f:
            name, score = line.strip().split(',')
            total += int(score)
            count += 1
    if count == 0:
        raise ValueError(f"File {path} has a header but no data rows")
    return total / count


if __name__ == '__main__':
    print('Q1 Snippet A:')
    snippet_a()
    print('Q1 Snippet B:')
    snippet_b()
    print('Q4 is_odd(3):', is_odd(3))
    print('Q4 product_of_odds_is_odd(15):', product_of_odds_is_odd(15))
