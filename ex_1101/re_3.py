import re

# 정규식을 이용한 문자열 내 문자 추출
x = 'My 2 favorite numbers are 19 and 42'
# y = re.findall('[0-8]+', x) # 0~8까지 숫자를 추출

y = re.findall('[a-z]+', x) # a~z까지 알파벳을 추출, 정규식은 대소문자 구분을 함

print(y)                    # 결과: 2, 1, 42 / y favorite numbers are and
