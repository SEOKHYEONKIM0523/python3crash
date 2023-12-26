# while 문
# 조건을 만족할 때 까지 반복을 실행
# 변수 = 초기값
# while 조건식 :
#   반복할 문장
#   변수 증가/감소

# 1 ~ 10 까지 모든 정수 출력
for i in range(1,11):
    print(i, end=' ')

i = 1 # 반복 초기값
while i <=10: # 반복 종료 조건
    print(i, end=' ')
    i += 1 # 반복 증감

# 1~50 까지 모든 정수 중 홀수만 출력
i=1
while i <= 50:
    print(i, end=' ')
    i += 2
i = 1
while i <= 50:
    if i % 2 != 0:print(i, end=' ')
    i += 1


# 1~50 까지 모든 정수 중 7의 배수만 출력
i = 1
while i <= 50:
    if i % 7 == 0 : print(i, end=' ')
    i += 1

# 1~200 까지 모든 정수의 합 출력
i=0
sum = 0
while i <= 200:
    sum += i
    i += 1
print(f'합계:{sum}')

# 1~100까지 모든 정수 중 3과 8의 공배수와 최소공배수 출력
i=1
mincm = 0
while i <= 100 :
    if i % 3 ==0 and i % 8 ==0 :
        print(i)
        if mincm ==0: mincm =i

    i += 1

print(mincm)

# 반복문 내 실행 중지 : break
# for , while 문 내에서 반복 흐름 벗어나기 위해 사용

# 1~10000 까지의 정수 합을 출력
# 정수 합이 12345678 보다 크면 계산을 중단한다
sum = 0
for i in range(1,10000+1):
    if sum > 12345678:
        print(i,sum)
        break
    sum  = sum + i


print(sum) # 49995000

i=1
sum=0
while i <= 10000:

    if sum > 12345678:
        print(i,end=' ')
        break
    sum += i
    i += 1
print(sum)

# 반복문 내 반복 건너뛰기 : continue
# for, while 문 내에서 반복 흐름을 일시적으로 건너뛰기 위해 사용
# 1~100 까지의 정수 합을 출력
# 단, 3의 배수나 7의 배수는 제외하고 합을 계산하세요

sum = 0
for i in range(1,100+1):
    if i % 3 == 0 or i % 7 == 0: continue
    sum  = sum + i
print(sum)

sum=0
i=0
while i < 100:
    i += 1
    if i % 3 == 0 or i % 7 == 0: continue
    sum += i

print(sum)


# 369게임
# 3 6 9 들어갈 때 짝!
i=1
while i < 100:
    if (i % 3 == 0 and i <=10):
        print(f'{i} 짝!')
    elif i==13 or i==16 or i==19 or i==23 or i==26 or i==29 or i==43 or i==46 or i==49 or i==53 or i==56 or i==59\
        or i==73 or i==76 or i==79 or i==83 or i==86 or i==89:
        print(f'{i} 짝!')
    elif i==33 or i==36 or i==39 or i==63 or i==66 or i==69 or i==93 or i==96 or i==99:
        print(f'{i} 짝! 짝!')
    elif (i>=30 and i<=39) or (i>=60 and i<=69) or (i>=90 and i<=99):
        print(f'{i} 짝!')
    else:
        print(i)
    i=i+1

for i in range(1,99+1):
    jjak = ''
    if '3' in str(i): jjak += ' 짝!'
    if '6' in str(i): jjak += ' 짝!'
    if '9' in str(i): jjak += ' 짝!'
    if i % 33 == 0 : jjak +=' 짝!'
    print(f'{i} {jjak}')


for i in range(1,99+1):
    if i <= 9:
        if i % 3 == 0: print(i, '짝!')
        else: print(i)
    else:
        print(i,end='')

        num1 = int(str(i)[0])
        num2 = int(str(i)[1])

        if num1 % 3 == 0: print(' 짝!',end=' ')
        if num2 != 0 and num2 % 3 == 0 : print('짝!',end=' ')
    print()

#오전 9시부터 오후 6시까지 교차 운행
trainA = 10
trainB = 25
trainC = 30

for m in range(1,540+1): # 오전 9시 ~ 오후 6시
    if m % 10 == 0 :
        if m % trainA == 0 and m % trainB == 0:
            print(f'{9 + m // 60:02d}시 {m % 60:02d}분')

        elif m % trainA == 0 and m % trainC == 0:
            print(f'{9 + m // 60:02d}시 {m % 60:02d}분')

        elif m % trainB == 0 and m % trainC == 0:
            print(f'{9 + m // 60:02d}시 {m % 60:02d}분')
        elif m % trainA == 0 and m % trainB == 0 and m % trainC ==0:
            print(f'{9 + m // 60:02d}시 {m % 60:02d}분')

# 관리자 로그인 기능
i=1
while i<=5:
    passwd = input('관리자 암호를 입력하세요')
    if passwd == 'hanbitac':
        print('로그인 됐습니다')
        break
    elif i==5:
        print('로그인실패!! 횟수 초과!!')
        break
    elif (passwd != 'hanbitac'):
        print('암호를 다시 확인하세요!')
    i=i+1



logincnt = 1
passwd = 'hanbitac'

while True:
    if logincnt > 5:
       print('로그인 실패! 횟수 초과!!')
       break

    pwd = input('관리자 암호를 입력하세요')

    if passwd != pwd:
        print('암호를 다시 확인하세요!')
        logincnt += 1
    else:
        print('로그인 됐습니다')
        break
