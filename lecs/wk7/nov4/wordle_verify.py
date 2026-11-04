"""
Date,Word,Num_guesses,Solved
2026-01-01,crane,4,True
2026-01-02,ghost,6,False
2026-01-03,plumb,3,True

    2026-01-04, zesty, 5, true

 2026-05-05 ,vivid      5,F
"""
raw = open('wordle.csv').readlines()
print(raw)
cols = len(raw[0].split(','))
correct = 0
for i in range(1, len(raw)):
    line = [i.strip().lower() for i in raw[i].split(',')]
    print(i, line)
    if len(line) == cols:
        # TODO: check if int is malformed
        correct += line[-1].lower() == 'true' and int(line[-2]) <= 6
        print(f'line {i} is {line[-1].lower() == 'true' and int(line[-2]) <= 6}')
    else:
        print(f'Line {i} is malformed, ignoring this line...')
print(f'{correct} correct')


# prof solution
with open('wordle.csv') as inpf:
    # Deal with the header
    inpf.readline() # Decision: just throw it away

    # Create some sort of data structure that contains the data I've read
    # Decision: Llist of lists
    records = []

    # Read the data, skipping blank lines
    # Decision: read one line at a time
    for line in inpf:
        # Decide what to do with malformed lines
        # Decision: emit warning, skip
        line = line.strip()
        if line == '':
            continue
        items = [item.strip() for item in line.split(',')]

        try:
            items[2] = int(items[2])
            if items[3].upper() == 'TRUE':
                items[3] = True
            elif items[3].upper() == 'FALSE':
                items[3] = False
            else:
                items[3] = None
            records.append(items)
        except ValueError:
            print('Warning: malformed line')
        except IndexError:
            print('Warning: malformed lines')
        if len(items) != 4:
            print('Warning: malformed line')
            continue

# Print how many times they successfully solved the wordle
successes = sum(record[3] for record in records)
print(successes)



records.append(['2026-11-04','split','5',True])
print(records)
# my solution: ','.join([str(i) for i in records[-1]])
# print(','.join([str(i) for i in records[-1]]))

# ==== prof solution
# Challenge 1: The records have to all be strings
lines = []
for record in records:
    record[2] = str(record[2])
    record[3] = str(record[3])
    lines.append(','.join(record))
print(lines)

# Challenge 2: You want to write one line at a time
# Use: join
with open('wordle_copy.csv', 'w') as outf:
    # outf.writelines(lines)
    outf.write('Date,Word,Num_guesses,Solved\n')
    outf.write('\n'.join(lines))
    outf.write('\n')
