# 반복문
# 특정 문장/코드를 지정한 횟수 / 조건에 의해 반복 실행하는 문장

# 간단한 메세지 한 번 출력
print('오늘 날씨 추워요!')

# 메시지를 여러 번 출력
print('오늘 날씨 추워요!')
print('오늘 날씨 추워요!')
print('오늘 날씨 추워요!')
print('오늘 날씨 추워요!')
print('오늘 날씨 추워요!')

# 메시지를 수정해야 할 필요가 생긴다면? - 수정하기 불편
print('오늘 날씨 너무 추워요!')
print('오늘 날씨 너무 추워요!')
print('오늘 날씨 너무 추워요!')

# 만약, 반복문을 사용한다면 ?
# 반복의 용이성과 수정의 용이성을 제공

# 파이썬의 반복문
# for : 지정한 횟수만큼 반복 수행
# while : 지정한 조건에 의해 반복 수행

# for문
# for 변수 in range(시작값, 종료값, 간격) "
#   반복할 문장
# 반복횟수는 range(시작값,종료값) 으로 유추 가능
# 즉, 횟수는 종료값 - 시작값 - 1 로 계산됨
# range 함수는 시작값과 종료값 -1 사이의 연속된 정수들을 반환함

# 1부터 10까지 정수 출력
print(1,2,3,4,5,6,7,8,9,10)

print(list(range(1,10+1)))

# 1부터 10까지 홀수 출력
print(list(range(1,10,2)))

# 이터러블(iterable) - 반복 가능한 객체 range 함수를 사용하여 범위 설정
# 값을 차례대로 꺼내서 볼 수 있는 객체를 의미
# 리스트, 튜플, 딕셔너리 등의 객체를 의미
# 반복문에 자주 사용함
#for i in range(1,10)
# => for i in [1,2,3,4,5,6,7,8,9]

# 반복문을 이용해서 메시지 출력
for i in range(1,4):
    print('오늘 날씨 추워요!')
# 1 ~ 10 까지 모든 정수 출력
 for i in range (1,10+1): # 1,2,3,4,...,9,10
     print(i, end = ",")

# 1~100 모든 정수의 합 출력
sum = 0
for i in range(1,100+1):
    print(i)
    sum = sum + i
print(sum)

# 1~N 까지의 합을 구하는 공식 : 가우스 덧셈 공식
# => (N * (N+1)) / 2
tot = (100 * (100+1)) / 2
print(tot)

# 구구단 중 특정 단을 입력 받아 출력
dan = int(input('몇 단인지 입력하시오.'))
for i in range (1,9+1):
    result = dan * i
    print(f'{dan} X {i} = {result}')
# 2~8사이 짝수 출력하기
for i in range(2,9,2):
    print(i,end=' ')

list(range(1, 12, 2))
list(range(0, 8, 2))
list(range(10, 0, -1))
list(range(1, 11, 2))

# 시작값이 없는 range함수
# 이럴 경우 시작값은 자동으로 0 부터 생성
list(range(1,10))
list(range(10))


# 이터러블에 문자열을 넣으면 아이템에는
# 문자열의 첫 문자부터 끝 문자가 순차적으로 저장됨
# 결과적으로 실행문은 문자 개수만큼 반복 실행됨

for c in 'hello':
    print(c,end="")

#이터너블에 리스트를 넣으면 아이템에는 리스트를 구성하는 요소들이 순차적으로 저장됨
#결과적으로 실행문은 리스트의 요소수만큼 반복 실행
menus = ['라면','돈까스','짜장면','냉면','정식']
for i in range(5):
    print(menus[i])
for menu in menus:
    print(menu)


# pass 키워드
# 반복문 사용 시 코드만 작성해 놓고 실행문은 나중에 추가하고 싶을 경우
# pass 라는 키워드를 사용

for i in range(1,100):
    pass     #반복할 내용은 나중에 작성

# 중첩반복문
# 두 개 이상의 반복문을 이용해서 반복실행을 할수도 있음
# 보통 2개의 반복문을 중첩해서 사용하는 경우가 많음
# 이 경우 바깥쪽 반복문은 행을,
# 안쪽 반복문은 열을 반복하는데 사용함
# 총 반복횟수는 (바깥쪽 반복문 횟수) * (안쪽 반복문 횟수)임


# *
# **
# ***
# ****
# ***** 모양 출력하기

for i in range(1,5+1):      #행
    for j in range(i): #열
        print('*',end='')
    print()                  #줄바꿈(새로운 행 만듦)


# 2단부터 9단까지의 구구단을 출력하는 반복문을 작성하세요

for i in range(2,9+1):
    for j in range(1,10):
        #줄바꿈 없이 출력하되
        #9개의 단을 출력하고 줄바꿈 추가
        # 자리수
        print(f'{i} x {j} = {i*j}', end=' ')
    print()


for i in range(1,10):
    for j in range(2,6):
        #줄바꿈 없이 출력하되
        #9개의 단을 출력하고 줄바꿈 추가
        # 자리수
        print(f'{j} x {i} = {i*j:2d}', end='  ')
    print()

for i in range(1, 10):
    for j in range(6, 10):
       print(f'{j} x {i} = {i*j:2d}', end='  ')
    print()



#employees를 이용해서 사원정보를 입력하면 list에 각각 저장하는 코드를 작성하세요
#사번empno, 이름fname, 성lname, 이메일email, 입사일hdate, 직책jobid,급여sal,부서번호deptid

empnos = []
fnames = []
lnames = []
emails = []
hdates = []
jobids = []
sals = []
deptids = []

empno = input('사번은?')
fname = input('이름은?')
lname = input('성은?')
email = input('이메일은?')
hdate = input('입사일은?')
jobid = input('직책은?')
sal = input('급여는?')
deptid = input('부서번호는?')

empnos.append(empno)
fnames.append(fname)
lnames.append(lname)
emails.append(email)
hdates.append(hdate)
jobids.append(jobid)
sals.append(sal)
deptids.append(deptid)

for i in range(len(empnos)):
    print(f'{empnos[i]} {fnames[i]} {lnames[i]}'
          f'{emails[i]} {hdates[i]} {jobids[i]}'
          f'{sals[i]} {deptids[i]}')

