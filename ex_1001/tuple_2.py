x = (3, 2, 1)
# x.sort()
# x.append(5)
# x.reverse()   error, 사용 불가

## list와 tuple의 내장 메소드
# l = list()
# dir(l)
# ['append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# dir(x)
# ['count', 'index']

# 좌변 우변 갯수가 일치해야함
(x, y) = (4, 'fred')
print(y)

(a, b) = (99, 98)
print(a)

# 함수에서 여러 값을 동시 반환
def t() :
    return (10, 20)
x, y = t()          # 소괄호 없이 콤마를 사용해도 튜플로 인식
print(x, y)
