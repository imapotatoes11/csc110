A = [2,4,6]
B = [1,2,3,4,5,6,7]

# Use all() and a comprehension-style generator to check
# whether A ⊆ B

# Hint: Create a sequence of True/False values, which represent
# whether an item in A is also in B
all(x in B for x in A)

# Write BOTH set-builder notation and a comprehension for
# "elements in B NOT in A" - compare to a loop that checks
# for differences.

# Set builder version: {x : x ∈ B, x ∉ A}
[x for x in B if x not in A]

# Challengge: write a comprehension for all pairs (x,y),
# x∈A, y∈B, x < y
[(x,y) for y in B for x in A if x < y]

# prof solution
[(x, y) for x in A for y in B if x < y]
