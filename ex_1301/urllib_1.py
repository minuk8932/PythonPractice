import urllib.request, urllib.parse, urllib.error

# 이전에 파일에서 데이터를 읽어왔던 것을 인터넷에서 읽어 옴
fhand = urllib.request.urlopen('https://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()

    for word in words:
        counts[words] = counts.get(word, 0) + 1

print(counts)
