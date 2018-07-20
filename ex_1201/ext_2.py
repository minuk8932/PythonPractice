line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

# email 호스트를 추출하는 다양한 방법1: split
words = line.split()
email = words[1]
piece = email.split('@')

print(piece[1])
