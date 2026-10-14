# Task: Create a python function is_function that accepts a
# set of 2-element tuples as a parameter, and returns True iff the
# relation is a function.
fn = {(1,2), (2,3), (3,5)}
rel = {(0,1),(1,2),(2,3),(3,4),(4,1),(5,2)}

is_function = lambda f : len(set(f)) == len(dict(f))
# yea this works

print(is_function(fn))
print(is_function({(1,2), (1,3), (2,3), (3,5)}))
print(is_function([(1, 2), (1, 2), (1, 3), (2, 3), (3, 5)]))
print(is_function(rel))
print(is_function({}))
print("-" * 20)

# prof solution
def is_function(relation: set) -> bool:
    """Return True iff relation is a mathematical function.
    """
    # Idea: Track elements of the domain that you have seen ...
    seen = set()
    for first_elem, second_elem in relation: # example item: (0, 1) ('cat', 'nice')
        # Check if we've seen the first element of the item before
        if first_elem in seen:
            return False
        seen.add(first_elem)
    return True

print(is_function({(0, 1), (1, 2), (2, 3), (3, 4), (4, 1), (5, 2)}))
print(is_function({}))
print(is_function({('cat', 'nice'), ('rabbit', 'nice'), ('dog', 'naughty'), ('cat', 'naughty')}))
print(is_function([(0, 1), (1, 2), (2, 3), (3, 4), (4, 1), (5, 2), (0, 1)]))
