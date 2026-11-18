def count_vowels(s: str) -> int:
    if not s:
        return 0
    if s[0].lower() in "aeiou":
        return 1 + count_vowels(s[1:])
    return count_vowels(s[1:])

def count_occurrences(lst: list[obj], x: obj) -> int:
    if not lst:
        return 0
    if lst[0] == x:
        return 1 + count_occurrences(lst[1:], x)
    return count_occurrences(lst[1:], x)

def is_sorted(lst: list[int]) -> bool:
    if len(lst) <= 1: return True
    if len(lst) == 2:
        return lst[0] < lst[1]
    
    if lst[0] > lst[1]: return False
    return is_sorted(lst[1:])

def reverse(s: str) -> str:
    if not s: return ""
    return reverse(s[1:]) + s[0]

def flatten(nested: list | int) -> list[int]:
    if type(nested) == int:
        return [nested]
    if not nested:
        return []
    return flatten(nested[0]) + flatten(nested[1:])

def max_depth(nested: list | int) -> int:
    if type(nested) == int:
        return 0
    if not nested: return 1
    return 1 + max(max_depth(item) for item in nested)


if __name__ == "__main__":
    print(count_vowels("strawberry"))
    print(count_occurrences(["a","b","a"], "a"))
    print(is_sorted([1,3,2,4,5]))
    print(reverse("stressed"))
    print(flatten([4, [7, [2]], 1]))
    print(max_depth([4, [7, [2]], 1]))
