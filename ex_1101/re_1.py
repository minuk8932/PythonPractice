import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    # 텍스트에서 같은 문자 패턴 찾기
    # if line.find('From:') >= 0:
    #     print(line)

    # 정규식을 이용한 문자 패턴 찾기
    if re.search('From:', line) :
        print(line)
