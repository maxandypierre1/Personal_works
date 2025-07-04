name = input("Enter file:")
fname = open(name)
lavi = dict()
vida = list()
for line in fname:
    if line.startswith("From "):
        line.rstrip()
        p = line.split(':')
        p = p[0].split()
        # print(p)
        p = p[5:]
        # print(p)
        for word in p:
            lavi[word] = lavi.get(word, 0) + 1
            # print(lavi)
for key, val in lavi.items():
    jouda = (key, val)
    vida.append(jouda)
    jouna = sorted(vida, reverse=False)
    # print(jouna)

for key, val in jouna:
    print(key, val)