# return true iff a provided list represents a matrix.
# a matrix -> the lengths of all the inner lists must all be equal

is_matrix = lambda lst: len(set([len(i) for i in lst])) == 1

print(is_matrix([[1,2,3],[4,5,6]]))
print(is_matrix([[1,2,3],[4,5]]))

# prof solution

matrix = [...]

is_matrix = True
for row in matrix:
    if len(row) != len(matrix[0]):
        is_matrix = False

total_items = 0
for row in matrix:
    total_items += len(row)
is_matrix = total_items % len(matrix) == 0
