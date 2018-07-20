import re

x = 'From: using the : character'
# greedy: 해당하는 문자열 중 가장 긴 것
# y = re.findall('^F.+:', x)
# non greedy : 해당하는 문자열 중 가장 짧은 것
y = re.findall('^F.+?:', x)
print(y)    # 결과: From:, From: using the :
