# we need to get the <p>...</p> before `<p>Defn...`

with open("pg29765-images.html", "r") as file:
    words = set()
    p = False
    raw = file.readline()
    true_out = []
    while raw:
        temp = []
        if "<p>" in raw:
            p = True
            temp.append(raw)
        if "</p>" in raw:
            p = False
            temp.append(raw[:raw.index("<")])
        if p:
            temp.append(raw)
        # print("".join(temp))
        if "".join(temp): true_out.append("".join(temp))
        raw = file.readline()


    import pprint
    # pprint.pprint(true_out)
    import re
    raw_words = [i for i in true_out if re.findall("\<p\>(\S+)\<br\>", i)]
    # pprint.pprint(raw_words)

    # get first occurence of >...< for each in `raw_words`
    for x in raw_words:
        for i in range(len(x)):
            if x[i] == "<":
                words.add(x[3:i])

    # pprint.pprint(words)

    true = set()

    for i in words:
        if i.isalpha() and len(i) == 5:
            true.add(i)
    # pprint.pprint(true)

    import random
    print("\n\n")
    print(len(true))
    print(random.choice([i for i in true]))

    with open("wordle.csv", "w") as out:
        out.write(",".join(true) + "\n")

# ==== prof sol
# ===============================================
with open('pg29765-images.html') as inpf:
    words = set()
    for line in inpf:
        line = line.strip()

        # How do I know it's a line of interest?
        # One idea?
        if len(line) == 12 and line[0:3] == '<p>' and \
            line[8:] == '<br>' and line[3:8].isalpha() and \
            line[3:8].upper() == line[3:8]:
            words.add(line[3:8])

print(len(words))

# select a couple of words
import random
words = list(words)
print(random.choice(words))

index = random.randint(0, len(words) -1 )
print(words[index])

random.shuffle(words)
print(words[0])
