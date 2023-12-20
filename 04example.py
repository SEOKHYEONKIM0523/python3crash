# 1
#프로그래밍 언어 실습 시 글꼴은 고정폭 글꼴을 사용할 것을 추천
print("☆     ☆      ☆☆        ☆☆☆☆☆    ☆☆☆☆☆     ☆       ☆          /////")
print("☆     ☆    ☆    ☆      ☆      ☆   ☆      ☆     ☆   ☆            | o o | ")
print("☆☆☆☆☆   ☆      ☆     ☆☆☆☆☆    ☆☆☆☆☆        ☆              (|  ^  |)")
print("☆     ☆   ☆☆☆☆☆☆     ☆      ☆    ☆      ☆      ☆              | [_] |")
print("☆     ☆   ☆       ☆    ☆       ☆   ☆        ☆    ☆                -----")

# 2
print('[ 음식나라 ]')
print('---------------------')
print('소주       1    12000')
print('너나치킨    2    6000')
print('---------------------')
print('과세합계         16200')
print('부가세           1800')
print('---------------------')
print('총합계           18000')
print('받은금액          50000')
print('잔돈             32000')
print('---------------------')
print('2014. 07 07 14:35:24')


# 3. 다음 중 자바 변수로 사용 가능한 것은 무엇인지 서술하여라.
# rate1, 1stPlayer, myprogram.java, long, TimeLimit, numberOfWindows
long , TimeLimit, numberOfWindows

# 학생 테이블의 각 컬럼 데이터도 변수로 선언하고 값으로 초기화
stno = 1
hakbun = 20350050
name = '김태희'
addr = '경기도 고양시'
birth = '1985.3.22'
deptid = 1
profid = 4
regdate = '2023-12-20 14:43:15'

print(stno, hakbun, name, addr, birth,deptid ,profid ,regdate)

#4 다음 수학식을 자바 표현식으로 바꿔보아라.
x, y, z = 1, 2, 3
s0, v0 , t, g = 4, 5, 6, 9.8
print(3 * x , 3 * x + 7 , ( x + y ) / 7, (3 * x + y) / ( z + 2) )
print(s0 + v0 * t + (1 / 2) * g * t ** 2 )

#5
print(1 / 3, (1 / 3) * 3)# 부동 소숫점 연산의 허점이 원인
print(7 / 3, 7 % 3, 7 // 3)

result = 2
result /= 2 #result = result / 2
print(result)

#6
x, y, m, n = 2.5, 1.5, 18, 4
print(x + n * y - (x + n) * y)
print(m / n + m % n )
print( 5 * x - n / 5)
print( 1 - (1 - ( 1 -(1 - (1 - n)))))
# 7
가:3+9+3.375=15.375
나:True
다:True
라:
마:7%4 + 3 - 2 / 6 *int(z)
사:3
아:False
자:False
차:7-54-12=-59

print(3 + 4.5 * 2 + 27 / 8)
print(True or False and 3 < 4 or not (5 == 7))
print(True or (3 < 5 and 6 >= 2))
print(not True > bool('a'))
print(7 % 4 + 3 - 2 / 6 * bool('Z'))
print('D' + 1 + 'M' % 2 / 3)
print(5.0 / 3 + 3 / 3)
print(53 % 21 < 45 / 18 )
print((4 < 6) or True and False or False and (2 > 3))
print(7 - (3 + 8 * 6 + 3) - (2 + 5 * 2))

# 9
가:True 나:True 다:True 라:True 마:True

print(True and False and True or True )  
print(True or True and True and False)   
print((True and False) or (True and not False) or (False and not False))
print((2 < 3) or (5 > 2) and not(4 == 4) or 9 not= 4)  
print(6 == 9 or 5 < 6 and 8 < 4 or 4 > 3)

# 10
가:float 나:float 다:float 라:False 마:float 아:str
print(27 / 13 + 4)
print( 27 / 13 + 4.0)
print(42.7 % 3 + 18  )
print(23 / 5 + 23 / 5.0 )
print( 2.0 + 'a') # 문자와 숫자간 연산 불가
print( 2 + bool('a')) 
print('a' + 'b')
print('a' / 'b') # 문자끼리 산술 연산 불가
#논리식과 산술식이 결합된 수식에서는 논리식 결과 True면 값이 출력, False면 False가 출력
print( (3 < 4) and (5 / 8))
print('a' and not 'b')

# 11
name = '홍길동'
weight = 32.5
age = 19
print(name,weight,age)

# 12
birthYear = 2005
currentYear = 2023

age = currentYear - birthYear
print('연나이 : ' , age)

# 13
print('7 x 1 =  7')
print('7 x 2 = 14')
print('7 x 3 = 21')
print('7 x 4 = 28')
print('7 x 5 = 35')
print('7 x 6 = 42')
print('7 x 7 = 49')
print('7 x 8 = 56')
print('7 x 9 = 63')
