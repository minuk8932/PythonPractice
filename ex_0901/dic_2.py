counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian','cwen']

# for in문을 통해 존재하지 않는 값에대한 접근을 막아줌
for name in names:
    if name in counts:      # 해당 이름이 count에 존재하는 경우
        counts[name] = counts[name] + 1
    else:           # 새로운 이름인 경우
        counts[name] = 1

print(counts)

# get 메소드를 통해 값이 존재하면 +1 아니면 0으로 초기화
for name in names:
    counts[name] = counts.get(name, 0) + 1

print(counts)
