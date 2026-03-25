#변수에 '철수'를 담기
name = '철수'
print(name)

#변수에 '영희'를 담기
name = '영희'
print(name)

PI = 3.1415
GRAVITY = 9.8

a = 11
b = 4
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)

a = 3
B = [1, 3, 5, 7, 9]

print(a in B)
print(a not in B)

CPUE = 4

if CPUE >= 6:
    print("자원풍부!")
elif 3<=CPUE<6:
    print("보통")
else:
    print("자원감소")
CPUE = 2

if CPUE < 3:
    print('자원감소')
elif CPUE > 6:
    print('자원풍부')
else:
    print('자원보통')

a = 5
if a < 5:
    print('a is smaller than 5')
elif a > 5:
    print('a is larger than 5')
else:
    print('a is 5')

integer_1 = 3214
integer_2 = -128109
float_1 = 12300.0
float_2 = 123.e2

print(integer_1, type(integer_1))
print(integer_2, type(integer_2))
print(float_1, type(float_1))
print(float_2, type(float_2))

print(integer_1 / integer_2, type(integer_1/integer_2))

import pandas as pd

# Window 환경에서는 encoding='cp949'
# MacOS 환경에서는 'utf-8'
character = pd.read_csv('/Users/jun/Library/Mobile Documents/com~apple~CloudDocs/Github/datamining/characters.csv', encoding='CP949')
character