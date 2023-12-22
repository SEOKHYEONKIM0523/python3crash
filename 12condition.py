# if 문
# 특정 조건을 만족하면 지정한 문장을 실행하는 조건문
# if 조건식:
#    수행할 문장

# 속도위반 체크 프로그램
# 기준속도 50km/h
speed = int(input("자동차의 현재 속도는 : "))
if speed >= 50:
    print('속도 위반!!')


# 파이썬의 코드 블록
# 특정한 동작을 위한 관련 코드를 한 곳에 모아 둔 것
# 이러한 코드들은 반드시 같은 들여쓰기 내에 존재해야 함

# 조건식이 True인 경우 무조건 코드블록을 실행함
if True: print('Hello python!')

# if ~ else 문
# if문은 조건이 참일 때만 지정한 코드를 실행하는데 비해
# if ~ else 문은 조건이 참일 때와 거짓일 때 각각 지정한 코드를 실행한다는 것이 다름
# if 조건식:
#   수행할 문장1
# else:
#  수행할 문장2

# 자동 온도 조절 프로그램
temp = int(input('기계 온도를 입력하세요. '))
if temp >= 40 :
    print('팬(Fan) 가동')
else:
    print('팬(Fan) 중지')


# 입력 받은 정수를 3으로 나누고
# 소숫점 첫 째 자리에서 반올림하기

num = int(input('정수를 입력하세요 : '))
result = num / 3
if result - int(result) >= 0.5:
    result = int(result) +1
else: result = int(result)

print(num, result)

# 중첩 if문
# if문 속에 또 다른 if문을 포함시켜 작성하는 조건문
# 조건문을 중첩할때는 들여쓰기에 유의해야 함
# 다양한 조건에 따라 결과를 처리하고 싶을때 사용 - 복잡함

# 평균이 73.5라 할때 조건에 따라
# 수/우/미/양/가 학점을
# 출력하는 조건문을 작성하세요

avg = 73.5

if avg >= 90:
    print('수')
else:
    if avg >= 80:
        print('우')
    else:
        if avg >= 70:
            print('미')
        else:
            if avg >=60:
                 print('양')
            else:
                print('가')


# 다중 if문
# 중첩 if문을 작성하는 경우 조건이 많으면 다소 복잡함
# 이러한 중첨 if문을 단순하게 작성할 수 있는 조건문

# if 조건식1:
#     실행할문장1
# elif 조건식2:
#     실행할문장2
# else:
#     실행할문장3

avg = 85.5

if avg >= 90:
    print('수')
elif avg >= 80:
    print('우')
elif avg >= 70:
    print('미')
elif avg >= 60:
    print('양')
else:
    print('가')

# 자동 주문 시스템 만들기

order = int(input('Good morning. Nice to meet you\n'
                  'Where are you from?\n'
                  'Please select a number\n'
                  '1.대한민국 2.USA 3.中國'))
if order == 1:
    print('주문하시겠어요?')
elif order == 2:
    print('Would you like to order?')
elif order == 3:
    print('您要点菜吗？')
else:print('Would you like to order?')

# bmi 지수에 따른 결과 출력
# 몸무게 / (키**2@)
weight = float(input('몸무게는? '))
height = float(input('키는? '))
bmi = weight / (height / 100) **2

if bmi >= 35: print('초고도비만')
elif bmi >= 30: print('고도비만')
elif bmi >= 25: print('비만')
elif bmi >= 23:print('과체중')
elif bmi >= 18.5: print('정상체중')
else: print('저체중')
print(f'{weight} {height} {bmi:.0f} {result}')

#가상 bmi
BMI = int(input('BMI지수를 입력해주세요. '))
if BMI > 140 :
    print('고도 비만')
elif BMI > 120:
    print('비만')
elif BMI > 110:
    print('과체중')
elif BMI > 90:
    print('정상 체중')
else:print('저체중')

# 누진세 적용 전기요금 계산
elec = float(input('전기 사용량을 입력하세요. '))

if elec > 400:
    print(f'사용량 : {elec} kwh\n'
          f'기본 요금 : 7300 원\n'
          f'단가 : 280.6원\n'
          f'전기 요금 : {elec*280.6+7300}원')
elif elec > 200:
    print(f'사용량 : {elec} kwh\n'
          f'기본 요금 : 1600 원\n'
          f'단가 : 187.9원\n'
          f'전기 요금 : {elec * 187.9 + 1600}원')
else:
    print(f'사용량 : {elec} kwh\n'
          f'기본 요금 : 910 원\n'
          f'단가 : 99.3 원\n'
          f'전기 요금 : {elec * 99.3 + 910}원')




# 현재년도가 각각 1992, 2000, 2020(윤)과
# 1900, 2100(윤x)에 대해 윤년여부를 출력하는
# 조건식을 작성하세요
# 윤년1 : 4로 나눠 나머지가 0이고
# 100으로 나눠 나머지가 0이 아니면
# 윤년2 : 400으로 나눠 나머지가 0

year = int(input('현재 년도를 입력하시오 :'))
isLeap = '윤년이 아닙니다'
cond1 = year % 4 == 0 and year % 100 != 0
cond2 = year % 400 == 0

if  cond1 or cond2:
    isLeap = '윤년 입니다'

print(f'{year} {isLeap}')

#차량 2부제 프로그램
num = int(input('차량 번호 4자리를 입력하세요. '))
date = int(input('오늘 날짜를 입력해주세요'))

if date % 2 == 0 and num % 2 == 0 :
    print('오늘 입차 : 번호가 짝수인 차량\n'
          '귀하의 차량은 입차 가능합니다')
elif date % 2 == 0 and num % 2 == 1:
    print('오늘 입차 : 번호가 짝수인 차량\n'
              '귀하의 차량은 입차 불가능합니다')

elif date % 2 == 1 and num % 2 == 1:
    print('오늘 입차 : 번호가 홀수인 차량\n'
          '귀하의 차량은 입차 가능합니다')
else:
    print('오늘 입차 : 번호가 홀수인 차량\n'
          '귀하의 차량은 입차 불가능합니다')

# 자동심장충격기 사용 시간에 따른 생존율 출력 프로그램
time = int(input('최초 장비를 사용하기까지 걸린 시간(초)을 입력하세요.'))
if time <= 60:
    print('생존율 : 85%')
elif time <= 120:
    print('생존율 : 76%')
elif time <= 180:
    print('생존율 : 66%')
elif time <= 240:
    print('생존율 : 57%')
elif time <= 300:
    print('생존율 : 47%')
elif  time > 360:
    print('생존율 : 25% 미만')
