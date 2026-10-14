"""CSC110 Lab 4: Exercises (Week 4 Review)

Complete the TODOs below. See the lab handout for full instructions.

WARNING: Do not modify the comments or variable names in this file.
Automated marking scripts will look for these exact names.

Exercises 2 and 5 are PROBE-ABLE PROBLEMS -- see the handout's "How to solve a
probe-able problem" section for info. To solve them, visit:

https://quickta.utm.utoronto.ca/?view=probeable-problem-set

And then select the "W5 Probeable Problems" Deployment.
"""

# =============================================================================
# Q1: Tracing list operations by hand (aliasing focus)
# =============================================================================
# : predicted print(a) in Snippet A -> [1,2,3,4]
# : predicted print(b) in Snippet A -> [1,2,3,4]
# : predicted print(c) in Snippet A -> [1,2,3]
# : predicted print(d) in Snippet A -> [1,2,3,4]
# : one-sentence explanation for the a/b pair: `b` is a pointer to a, so calling b.append(4) calls the .append(4) on the list assigned ot `a`
# : one-sentence explanation for the c/d pair: the slicing operation `[:]` creates a copy of the list `c`, so any operation on d will be done on d alone.
# : predicted print(original) in Snippet B -> [10, 20, 30]
# : one-sentence explanation for why add_item can affect original: the function is given an alias/pointer to the original list, thus the `append` modifies the orignal list

def snippet_a() -> tuple[list[int], list[int], list[int], list[int]]:
    """Run Snippet A from the handout and return (a, b, c, d) after both
    mutations for verification purposes.

    >>> snippet_a()
    ([1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3], [1, 2, 3, 4])
    """
    a = [1, 2, 3]
    b = a
    b.append(4)

    c = [1, 2, 3]
    d = c[:]
    d.append(4)

    return a, b, c, d


def snippet_b() -> list[int]:
    """Run Snippet B from the handout and return `original` after the call
    to add_item for verification purposes.

    >>> snippet_b()
    [10, 20, 30]
    """
    def add_item(lst, item):
        lst.append(item)

    original = [10, 20]
    add_item(original, 30)
    return original


# =============================================================================
# Q2 -- PROBE-ABLE: Grade roster summary
# =============================================================================
# TODO Q2 SPEC NOTES: (write at least 3 specific facts you learned from
# probing the spec and roughly what question got you each one)
#  1. the summary statistic is the average grade for each student
#  2. Empty grades (None) are considered 0 in the calculation
#  3. The result should be rounded down to the nearest integer

def summarize_student_grades(grades: list[list]) -> list[int]:
    """You must probe the spec before you'll know the exact rules.
    """
    # : implement per the probed specification.
    return [
        int(sum(0 if grade is None else grade for grade in student) // len(student))
        if student else 0
        for student in grades
    ]


# =============================================================================
# Q3: Debugging & reasoning practice
# =============================================================================

# --- Item 1: aliasing bug ---
# : does get_top_scores_fixed's docstring promise hold? explain why the
# ORIGINAL (buggy) version from the handout breaks that promise.
# the .sort() method is called on an alias/pointer of the original caller's list, modifying that original object.

def get_top_scores_fixed(scores: list[int]) -> list[int]:
    """Return the top 3 scores. Fixed version of the buggy get_top_scores 
    from the handout.

    >>> nums = [55, 88, 42, 91, 67]
    >>> get_top_scores_fixed(nums)
    [91, 88, 67]
    >>> nums
    [55, 88, 42, 91, 67]
    """
    # : write a corrected version here
    return sorted(scores, reverse=True)[:3]


# --- Item 2: set-difference direction bug ---
# : what's backwards in the handout's `missing` expression, and what's
# the corrected version? (write the corrected set expression as a comment)
# The handout's `completed_quiz - enrolled` is backwards. It should be `enrolled - completed_quiz`

def students_missing_quiz(enrolled: set, completed_quiz: set) -> set:
    """Return the students in `enrolled` who are NOT in `completed_quiz`.
    Fixed version of the buggy `missing` computation from the handout.

    >>> sorted(students_missing_quiz({'Alice', 'Bob', 'Carol', 'Dave'}, {'Alice', 'Carol'}))
    ['Bob', 'Dave']
    """
    # : write a corrected version here
    return enrolled - completed_quiz


# --- Item 3: membership-vs-subset mix-up ---
# : what does `newsletter_subscribers in all_students` actually check?
# why does it silently evaluate to False rather than raising an error?
# The expression actually checks if the set `newsletter_subscribers` is in `all_students` (ie an actual set() object in the all_students set)

def all_subscribers_are_students(newsletter_subscribers: set, all_students: set) -> bool:
    """Return whether every subscriber is a student. Fixed version of the
    buggy `in`-based check from the handout.

    >>> all_subscribers_are_students({'Alice', 'Bob'}, {'Alice', 'Bob', 'Carol', 'Dave'})
    True
    >>> all_subscribers_are_students({'Alice', 'Eve'}, {'Alice', 'Bob', 'Carol', 'Dave'})
    False
    """
    # : write a corrected version here
    return newsletter_subscribers - all_students == set()


# --- Item 4: list comprehension filter bug ---
# : what does the handout's buggy doubled_negatives actually compute?
# what one-character change fixes the filter condition?
# The handout's snippet actually doubles all positive values instead of negatives

def double_negatives_fixed(temps: list[int]) -> list[int]:
    """Return a list with every negative temperature doubled. Fixed version 
    of the buggy doubled_negatives from the handout.

    >>> double_negatives_fixed([-5, 3, -2, 8, -10, 1])
    [-10, -4, -20]
    """
    # : write a corrected version here.
    return [x * 2 for x in temps if x < 0]


# =============================================================================
# Q4: The subset-proof technique, by hand and in code
# =============================================================================
# : (1) arbitrary element of A∩B
# : (2) (the connective joining x in A and x in B) `and`
# : (3) x is in A
# : (4) (what we've shown, in words or symbols) we've shown A∩B⊆A

def is_subset(A: set, B: set) -> bool:
    """Return whether A is a subset of B, i.e. every element of A is also
    in B. Do NOT use Python's built-in <= operator or .issubset() method --
    write the loop yourself (mirroring the arbitrary-element proof template
    from part (a)).

    >>> is_subset({3, 4}, {1, 2, 3, 4})
    True
    >>> is_subset({1, 2, 3, 4}, {3, 4, 5, 6})
    False
    >>> is_subset(set(), {1, 2, 3})
    True
    """
    # : implement using a loop (no <= or .issubset()).
    # return all([i in B for i in A])
    for i in A:
        if i not in B:
            return False
    return True


# : using is_subset, verify that A & B is a subset of A for
# A = {1, 2, 3, 4}, B = {3, 4, 5, 6}. Store the boolean result below.
intersection_is_subset_of_a = is_subset({1, 2, 3, 4} & {3, 4, 5, 6}, {1, 2, 3, 4})  # True


# =============================================================================
# Q5 -- PROBE-ABLE: Campus roster overlap report
# =============================================================================
# TODO Q5 SPEC NOTES: (write at least 3 specific facts you learned from
# probing the spec and roughly what question got you each one)
#  1. utm, utsg, and utsc are sets of strings. each string is a student's name
#  2. Return a list containing four sets, in this order:
#       Students in both UTM and UTSG
#       Students in UTM but not UTSG
#       Students in UTSG or UTSC, but not UTM
#       All students from UTM, UTSG, or UTSC
#  3. compare strings as-is (no lowercase, no strip, etc.)

def create_campus_list(utm: set, utsg: set, utsc: set) -> list[set]:
    """Return the registrar's campus-overlap reports for the three campus sets.

    You must probe the spec before you'll know the exact rules.
    """
    # : implement per the probed specification.
    return [
        utm & utsg,
        utm - utsg,
        (utsg | utsc) - utm,
        utm | utsc | utsg
    ]


if __name__ == '__main__':
    print('Q1 snippet_a():', snippet_a())
    print('Q1 snippet_b():', snippet_b())
    print('Q2 summarize_student_grades:', summarize_student_grades([[90, 80, 90, 80]]))
    print('Q3 get_top_scores_fixed:', get_top_scores_fixed([55, 88, 42, 91, 67]))
    print('Q3 students_missing_quiz:', students_missing_quiz({'Alice', 'Bob', 'Carol', 'Dave'}, {'Alice', 'Carol'}))
    print('Q3 all_subscribers_are_students:', all_subscribers_are_students({'Alice', 'Bob'}, {'Alice', 'Bob', 'Carol', 'Dave'}))
    print('Q3 double_negatives_fixed:', double_negatives_fixed([-5, 3, -2, 8, -10, 1]))
    print('Q4 is_subset({3,4}, {1,2,3,4}):', is_subset({3, 4}, {1, 2, 3, 4}))
    print('Q4 intersection_is_subset_of_a:', intersection_is_subset_of_a)
    print('Q5 create_campus_list:', create_campus_list({'Bob'}, {'Bob'}, {'Bob'}))
