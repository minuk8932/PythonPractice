han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.split();
    # print('Words: ',wds) : debug

    # Gardian Pattern
    # if len(wds) < 1:
    #     continue;

    # Gardian in a compound statement
    if len(wds) < 3 or wds[0] != 'From':
        # print('Ignore') : debug
        continue

    print(wds[2])
