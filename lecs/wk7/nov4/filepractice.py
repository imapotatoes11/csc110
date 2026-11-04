# File fname
'''Hi

I am a file
with some

    blank lines and
  spaces!
'''
# q1
with open('fname', 'r') as inpf:
    lines = inpf.readlines()
    print(len(lines))
    print(lines)

# q2
with open('fname', 'r') as inpf:
    lines = inpf.read().split('\n')
    print(len(lines))
    print(lines)

# q3
with open('fname') as inpf:
    with open('fname', 'w') as outf: # this line overwrites the file to empty! so the question returns `1`
        lines = inpf.readlines()
        lines.append("Final line of the file\n")
        outf.writelines(lines)

with open('fname', 'r') as inpf:
    lines = inpf.readlines()
    print(len(lines))
