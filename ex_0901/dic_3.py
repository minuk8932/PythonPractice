counts = {'chuck': 1, 'fred': 42, 'jan': 100}
for key in counts:
    print(key, counts[key])

# key만 탐색
print(list(counts))
print(counts.keys())

# 값만 탐색
print(counts.values())

# 튜플을 이용한 값과 키를 쌍으로 리스트로 변환 출력
print(counts.items())

for k, v in counts.items():
    print(k, v)
