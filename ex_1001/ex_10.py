fname = input('Enter File: ')

if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()

for line in hand:
    line = line.rstrip()
    words = line.split()

    for w in words:
        di[w] = di.get(w, 0) + 1

print(di)

tmp = list()
for k, v in di.items():
    newt = (v, k)
    tmp.append(newt)

# print('Flipped', tmp)

tmp = sorted(tmp)
# tmp = sorted(tmp, reverse = True)
# print('Sorted', tmp[:])

for v, k in tmp[:5]:
    print(k, v)
