# tuple은 소괄호()를 통해 선언, 변경 불가능(immutable)한 속성을 가짐
# 리스트와 유사 순서가 있고, 인덱스로 접근 가능

x = ('Glenn', 'Sally', 'Joseph')
print(x[2])
# Joseph
y = ( 1, 9, 2 )
print(y)
# (1, 9, 2)
print(max(y))

for iter in y:
    print(iter)

# 튜플: 변경 불가,
# TypeError: 'tuple' object does not support item assignment
# x = (9, 8, 7)

# 리스트: 변경 가능
x = [9, 8, 7]
x[2] = 6
print(x)
