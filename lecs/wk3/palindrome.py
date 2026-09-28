word = "racecar"
word = "palindrome"
is_palindrome = False
for i in range(len(word) // 2):
    if word[i] == word[-(i + 1)] and not is_palindrome:
        is_palindrome = True
    if word[i] != word[-(i + 1)]:
        is_palindrome = False
print(is_palindrome)

print(not (False in [word[i] == word[-(i + 1)] for i in range(len(word) // 2)]))

# prof sol
word = "racecar"
print(f"Is {word} a palindrome? {word == word[::-1]}")

is_palindrome = True
for i in range(len(word)):
    if word[i] != word[-1 - i]:
        is_palindrome = False
print(f"Is {word} a palindrome? {is_palindrome}")
