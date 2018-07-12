words = 'Connect Foundation'

if 'F' in words:
  words.lower()
  words[7] = '&' # 'str' object does not support item assignment
else:
  print(words)
print(words)
