# 할인된 상품 가격 출력 프로그램

products = {'쌀':9900, '상추':1900, '고추':2900, '마늘':8900, '통닭':5600, '햄':6900, '치즈':3900}
# print(f'''
# ---------------------------------------
# -- 한빛마트 오늘의 할인 가격표 출력 시스템 --
# ---------------------------------------
# ''')
#
# rate = int(input('오늘의 할인율을 입력하세요.'))
#
# prices = []
# for val in products.values():
#     price = val * (1 - (rate/100)) # 할인율에 따른 할인금액 계산
#     prices.append(price)
#
#
# for idx, key in enumerate(products.keys()):
#     print(f'{key:3s} : {products[key]} 원 / {rate}% 할인 => {prices[idx]:.0f} 원')
#

def readDiscount():
    print(f'''
    ---------------------------------------
    -- 한빛마트 오늘의 할인 가격표 출력 시스템 --
    ---------------------------------------
    ''')

    rate = int(input('오늘의 할인율을 입력하세요.'))

    return rate


def getDiscountPrice(rate):
    prices = []
    for val in products.values():
        price = val * (1 - (rate / 100))  # 할인율에 따른 할인금액 계산
        prices.append(price)
    return prices

def printDiscountPrice(rate,prices):
    for idx, key in enumerate(products.keys()):
        print(f'{key:3s} : {products[key]} 원 / {rate}% 할인 => {prices[idx]:.0f} 원')

rate = readDiscount()
prices = getDiscountPrice(rate)
printDiscountPrice(rate,prices)


#26. 사용자가 연봉과 결혼 여부를 입력하면 다음의 세금율에 의해 납부해야 할 세금을 계산하는 프로그램을 작성하세요 (Tax)
#가. 미혼인 경우 : 연봉 3000미만 - 10%,  연봉 3000이상 - 25%
#나. 결혼한 경우 : 연봉 6000미만 - 15%,  연봉 6000이상 - 35%

# isMarried = input('결혼 여부는 ? (1: 미혼 2: 기혼)')
# sal = int(input('연봉은? '))
#
# if isMarried == '1':
#     if sal >= 3000: tax = sal * 0.25
#     else : tax = sal * 0.1
# else:
#     if sal >= 6000: tax = sal * 0.35
#     else: tax = sal * 0.15
#
# print(f'{isMarried} {sal} {tax}')

def readInfo():
    isMarried = input('결혼 여부는 ? (1: 미혼 2: 기혼)')
    sal = int(input('연봉은? '))

    return isMarried, sal

def computeTax(isMarried,sal):
    if isMarried == '1':
        if sal >= 3000: tax = sal * 0.25
        else : tax = sal * 0.1
    else:
        if sal >= 6000: tax = sal * 0.35
        else: tax = sal * 0.15

    return tax

isMarried, sal = readInfo()
tax = computeTax(isMarried,sal)
print(f'{isMarried} 연봉:{sal}만원 세금:{tax:.0f}만원')

from hangleUtil import preFormat

def printDiscountPrice2(rate,prices):
    for idx, key in enumerate(products.keys()):
        print(f'{preFormat(key,5)} : {preFormat(str(products[key]),6)} 원 / {preFormat(str(rate),3)}% 할인 => {preFormat(str(prices[idx]),6)} 원')
rate = readDiscount()
prices = getDiscountPrice(rate)
printDiscountPrice2(rate,prices)


# 변수의 유효범위 : scope
# 지역변수 : 블럭내에 선언한 변수, 특정 블럭내에서만 유효
# 전역변수 : 소스내에 선언한 변수, 모든 범위에서 유효
# 함수 내에서 선언한 변수는 함수 밖에서 접근 가능?
# => 함수내에서 선언한 변수는 함수내에서만 사용가능

num1 = 10 # 전역변수 global
print(num1) # 전역 변수 출력

def func1():
    global num3 # global 지역변수를 전역변수로 선언
    num2 = 100 # 지역 변수
    num3 = 999 # 지역 변수

    print(num1) # 함수 내에서 전역변수 출력
    print(num2) # 함수 내에서 지역변수 출력
    print(num3)

func1()
print(num2) #  func1함수내에 선언된 지역변수 출력 - 오류 발생
print(num3) #  func1함수내에 global 지역변수 출력 - 정상 출력

# 만일, 함수내에서 전역변수의 값을 수정하고 싶다면?
# => global 문 사용 (비추!)
# => 매개변수, return문 사용 (추천!)

num1 = 99
num2 = 'abc'
def func2():
    global num2 #전역변수를 함수 내에서 수정하기 위해 global로 선언
    num1 = 77
    num2 = 'xyz' # 전역변수를 함수 내에서 수정 , 수정한 내용이 함수 밖에서도 유지될까?
    print(num1)
    print(num2)

func2()
print(num1)
print(num2) # 함수 내에서 수정한 값이 밖에서도 유지 됨

# call by value vs call by reference
# 파이썬에서는 기본 자료형 변수는 함수의 매개 변수로 넘기는 경우
# call by value(값에 의한 호출)이 발생하기 때문에 함수 내 매개변수와 호출 시
# 전달한 변수는 서로 다른 것으로 인식됨

# 반면, 참조 자료형 변수를 함수의 매개 변수로 넘기는 경우
# call by reference(주소에 의한 호출)이 발생하기 때문에
# 함수 내 매개변수와 호출시 전달한 변수는 서로 동일한 것으로 인식됨

# 단, 파이썬은 call by value/reference 라기 보다
# passed by assignment(어떤 값을 전달하느냐에따라)로 다뤄지고 있음


# 웹사이트 방문 횟수 조회 프로그램
num=0
while True:
    website = int(input('1.웹사이트 방문, 2.종료'))
    if website == 1:
        num += 1
        print('누적 방문 횟수 :', num)
    else:
        break

# visits = 0 # 방문 횟수
# while True:
#     job = input('작업은? (1.웹사이트 방문, 2.종료)')
#     if job == '1':
#         visits += 1
#         print('누적 방문 횟수 : ', visits)
#     elif job == '2':
#         break

visits =0
def visitTime():

    # visits = 0 # 방문 횟수
    global visits # 전역 변수
    while True:
        job = input('작업은? (1.웹사이트 방문, 2.종료)')
        if job == '1':
            visits += 1
            print('누적 방문 횟수 : ', visits)
        elif job == '2':
            break
visitTime()



# 주민번호를 입력받아 유효성을 검사하는
# checkJumin 함수를 작성하세요
# 1. 주민번호 맨 끝자리를 제외한 나머지 번호들의
#    각자리를 2,3,4,5,6,7,8,9,2,3,4,5 가중치로 곱합
# 2. 곱한 결과를 각각 모두 더함
# 3. 더한 값을 11로 나눠 구한 나머지를 11에서 뺌
# 4. 이렇게 구한 결과와 주민번호 맨 마지막 자리의 일치여부 검사
# 5. 만약, 구한 결과가 2자리라면 맨 끝자리와 비교함

# jumin = input('주민번호를 입력하세요 : ')
#
# sum = 0
#
# sum += int(jumin[0]) * 2
# sum += int(jumin[1]) * 3
# sum += int(jumin[2]) * 4
# sum += int(jumin[3]) * 5
# sum += int(jumin[4]) * 6
# sum += int(jumin[5]) * 7
# sum += int(jumin[7]) * 8
# sum += int(jumin[8]) * 9
# sum += int(jumin[9]) * 2
# sum += int(jumin[10]) * 3
# sum += int(jumin[11]) * 4
# sum += int(jumin[12]) * 5
#
# mod = sum % 11
# checker = 11 - mod
# print(checker)
#
# if checker == int(jumin[13]):
#     print('주민번호 유효!')
# else:
#     print('주민번호 틀림')

def checkJumin():
    jumin = input('주민번호를 입력하세요 : ')
    sum = 0
    result = '주민번호 불일치'


    sum += int(jumin[0]) * 2
    sum += int(jumin[1]) * 3
    sum += int(jumin[2]) * 4
    sum += int(jumin[3]) * 5
    sum += int(jumin[4]) * 6
    sum += int(jumin[5]) * 7
    sum += int(jumin[7]) * 8
    sum += int(jumin[8]) * 9
    sum += int(jumin[9]) * 2
    sum += int(jumin[10]) * 3
    sum += int(jumin[11]) * 4
    sum += int(jumin[12]) * 5

    mod = sum % 11
    checker = 11 - mod
    if checker == int(jumin[13]): result = '주민번호 유효'
    print(result)

checkJumin()

def checkJumin2():
    sum = 0
    result = '주민번호 불일치'
    jumin = input('주민번호를 입력하세요 : ')
    pos = [0,1,2,3,4,5,7,8,9,10,11,12]
    weight = [2,3,4,5,6,7,8,9,2,3,4,5]

    for i in range(len(pos)):
        sum += int(jumin[ pos[i] ]) * weight[i]

    checker = (11 - (sum % 11) % 10)
    if checker == int(jumin[13]): result = '주민번호 유효'

    print(result)

checkJumin2()
