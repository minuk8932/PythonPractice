counts = {'chuck': 1, 'fred': 42, 'jan': 100}
for key in counts:
    print(key, counts[key])

# key만 탐색
print(list(counts))
print(counts.keys())

# 값만 탐색
print(counts.values())
