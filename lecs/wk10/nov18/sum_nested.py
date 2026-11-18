def sum_nested(nested: list | int) -> int:
    s = 0
    for i in nested:
        """
        if type(i) == int:
            s += i
        else:
            s += sum_nested(i)
        """
        if isinstance(i, list): # `isinstance()` is idiomatic
            s += sum_nested(i)
        else:
            s += i
    return s

if __name__ == "__main__":
    demo = [4, [7, [2]], 1]
    print(sum_nested(demo))
