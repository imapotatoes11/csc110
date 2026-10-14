# ec = equivalence class
words = ["listen", "silent", "enlist", "banana", "eat", "tea", "ate"]

# Task: Build a partition for words.
# The relation is "is an anagram of"

def is_anagram(word1, word2):
  """Return True iff word1 is an anagram of word2
  """
  w2_letters = list(word2)
  for ch in word1:
    if ch in w2_letters:
      w2_letters.remove(ch)
    else:
      return False
  return len(w2_letters) == 0

# alternate
# sorted(word1) == sorted(word2)

words = ["listen", "silent", "enlist", "banana", "eat", "tea", "ate"]
partition = []

for word in words:
  # Determine which words are equivalent to your current word, build a set
  ec = set()
  for word2 in words:
    if is_anagram(word, word2):
      ec.add(word2)  
  partition.append(ec)

print(partition)

# Ideas for fixing this?
# Keep partition as a set. Add tuples to it. (convert set to tuple.)
# Keep partition a list. Check whether a set is in the list before adding it
# Make partition a dictionary. Sorted letters are the key, ec is the value.
# Remove word2 from words when you add it to an ec.

# ----------------------------------
# Define a relation on integers:
# a ~ b if |a| = |b| (same aboslute value).

# Task: build the equivalence classes for this relation given a set of integers.

L = [-3, 0, 4, -7, 6, 3, -6]
partition = {} # key: abs(item), value: items in the equivalence class

# Look at items, one at a time.
for item in L:
  ec = partition.setdefault(abs(item), set())
  ec.add(item)

print(partition)
