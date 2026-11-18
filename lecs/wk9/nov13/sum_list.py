lst = [1,2,3,4,5,6,7,8,9]
def sum_lst(n: list) -> int:
    if not n:
        return 0
    return n[0] + sum_lst(n[1:])

print(sum_lst(lst))


# prof solution
def sum_list(L: list[int]) -> int:
    '''Return the sum of the items in L.

    >>> sum_list([3, 4, 5])
    12
    '''
    if len(L) == 0:
        return 0
    return L[0] + sum_list(L[1:])

