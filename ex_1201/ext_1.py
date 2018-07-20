
# email 호스트를 추출하는 다양한 방법1: find & list slicing
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')

print(atpos)    # 21, '@'의 인덱스 값

sppos = data.find(' ', atpos)
print(sppos)    # 34, '@'다음으로 나오는 공백의 인덱스 값

host = data[atpos+1 :sppos]
print(host)     # uct.ac.za
