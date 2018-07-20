import re

# email 호스트를 추출하는 다양한 방법3: regular expression
lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# y = re.findall('@([^ ]*)',lin)
y = re.findall('^From .*@([^ ]*)',lin)

print(y)
