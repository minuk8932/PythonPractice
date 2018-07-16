# key 기준 정렬

d = {'b': 1, 'a': 10, 'c': 22}

for k, v in sorted(d.items()):
    print(k, v)

tmp = list()
for k, v in d.items():
    tmp.append((v, k))

print(tmp)

tmp = sorted(tmp)           # 오름차순
# tmp = sorted(tmp, reverse=True)  내림차순
print(tmp)
