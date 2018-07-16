fname = input('Enter File: ')

# 파일 이름에 아무것도 치지 않을 경우 clown.txt를 담아줌
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()

# 해당 파일을 한 줄씩 받아 개행 문자를 제거하고, words에 단어별로 잘라 저장 후 출력
for line in hand:
    line = line.rstrip()
    # print(line)
    words = line.split()    # list
    # print(words)

    for w in words:
        # 처음 등장한 값인 경우 -99가 출력됨
        # print('**', w, di.get(w, -99))

        # if the key is not there the count is zero
        # oldCount = di.get(w, 0)
        # print(w, 'old', oldCount)
        #
        # newCount = oldCount + 1
        # di[w] = newCount

        # idiom: retrieve /create/update counter
        di[w] = di.get(w, 0) + 1
        # print(w, 'new', di[w])

        # print(w)        # key
        # if w in di :        # dic에 존재하는 경우 +1 아니라면 1로 초기화
        #     di[w] = di[w] + 1
        #     # print('**Existing**')
        # else:
        #     di[w] = 1
            # print('**NEW**')
        # print(di[w])    # value

        # print(w, di[w])

# print(di)

#now we want to find the most common word
largest = -1
theWord = None

for k, v in di.items():
    print(k,v)

    if v > largest:
        largest = v
        theWord = k # cature/remember the word that was largest

print('Done', largest, theWord)
