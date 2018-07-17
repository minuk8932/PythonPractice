import re

hand = open('mbox-short.txt')

for line in hand:
    line = line.rstrip()

    # From으로 시작하는 문장을 찾음
    # if line.startswith('From:'):
        # print(line)

    # 정규식을 통해 From으로 시작하는 문장을 찾음
    if re.search('^From:', line):
        print(line)
