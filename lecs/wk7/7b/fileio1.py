# 1. Write a short program that asks the user for 3 words and writes each on its own line to words.txt

with open("words.txt", "w") as f:
    f.writelines([i + '\n' for i in input("enter 3 words (space separated): ").split()])

# 2. Write a program that reads words.txt and prints each line in uppercase

with open("words.txt") as f:
    print("\n".join([i.strip().upper() for i in f.readlines()]))

# 3. Add a 4th word to words.txt WITHOUT rewriting the first 3 - use the right mode.

open("words.txt", "a").write("Apple\n")

# ==================================================
# prof solution

# 1
word1 = input()
word2 = input()
word3 = input()
with open('words.txt', 'w') as outf:
    outf.writelines([word1 + '\n', word2 + '\n', word3 + '\n'])

# 2
with open('words.txt') as inpf:
    for line in inpf:
        print(line[:-1].upper())

# 3
with open('words.txt', 'a') as outf:
    outf.write('word4\n')
