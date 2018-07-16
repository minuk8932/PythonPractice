fhand = open('romeo.txt')

counts={}
for line in fhand:
    words = line.split()

    for w in words:
        counts[w] = counts.get(w, 0) + 1

lst = []
for k, v in counts.items():
    newtup = (v, k)
    lst.append(newtup)

lst = sorted(lst, reverse= True)    # 내림차순 정렬


for v, k in lst[:10]:
    print(k, v)
