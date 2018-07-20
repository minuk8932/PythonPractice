import re

# 공백을 제외하고 @ 전 후의 문자열 뽑아내기
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

# y = re.findall('\S+@\S+', x)
y = re.findall('^From (\S+@\S+)', x)
print(y)    # 둘은 같은 결과: stephen.marquard@uct.ac.za
