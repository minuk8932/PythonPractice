name = input('Enter file: ')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()

    for word in words:
        counts[word] = counts.get(word, 0) + 1

# print(counts)

bigCount = None
bigWord = None

for w, c in counts.items():
    if bigCount is None or c > bigCount:
        bigWord = w
        bigCount = c

print(bigWord, bigCount)
