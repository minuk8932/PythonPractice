import re

hand = open('mbox-short.txt')
numlist = list()

for line in hand:
    line = line.rstrip()
    # X-DSPAM-Confidence 이후 나오는 숫자를 비교해 큰 숫자를 계속 출력
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1: continue

    num = float(stuff[0])
    numlist.append(num)
    print('Maximum: ', max(numlist))

# ref: 특수문자를 정규식에 인식 시키는 방법
# x = 'We just received $10.00 for cookies'
# y = re.findall('\$[0-9.]+',x)
#
# print(y)
