# 조건문
# 주어진 상황에 따라 적절한 명령문을 수행하는 문장
# 프로그래밍에서 조건을 판단하여
# 해당 조건에 맞는 상황을 수행하는데 사용됨
import operator

# 조건문 작성시 반드시 들여쓰기(탭)에 따라 문장을 작성해야 함
# 조건문은 일반적으로 비교연산자나 논리연산자를
# 이용한 표현식으로 구성
# 비교연산자 : x > 100, y != 123
# 논리연산자 : (x > 100) and (y != 123)

# 조건 연산자
# 일반적인 조건문 (if ~ else)을 한 줄로 표현한 것
# 조건식이 참일 때 값 if 조건식 else 거짓일 때 값

# 수입, 지출을 입력받아 흑자/적자 여부 출력

income = int(input("수입은? "))
outcome = int(input("지출은? "))
result = '흑자' if (income > outcome) else '적자'
print(f'수입:{income}, 지출:{outcome}, {result}')

# 긴급 재난 지원금 대상자 판별
# 조건1 : 소득 기준 4,000,000 이하
# 조건2 : 다른 지원금을 받지 않는 세대

income = int(input('월 소득을 입력하세요. '))
other = int(input('다른 지원금을 받고 있습니까? 1번 받고있다. 2번 받고 있지 않다. '))
isTarget = income <=4_000_000 and other == 2
result = '수급 대상자' if isTarget  else '수급 대상자가 아닙니다.'
print(f'{result}')

# 모듈
# 타인이나 조직이 만든 특정 기능을 모아둔 파일
# 모듈을 사용하려면 import 키워드 사용

# operator 모듈 사용하기
# 연산자를 사용했을 때보다 실행 속도가 빠름
# add/sub/mul/truediv/mod/floordiv/pow
# eq/ne/gt/ge/lt/le
# and_/or_/not_

import operator as op


#isTarget = income <=4_000_000 and other == 2
isTarget = op.and_(op.le(income, 4000000),
                       op.eq(other,2))


## 업무 컴퓨터 수량 파악
# 하루 업무 처리 : 3대의 컴퓨터로 8시간 근무
# 근무시간이 줄었을때 필요한 컴퓨터 대수 파악

import operator
time = int(input("근무시간을 입력하세요"))
result = operator.truediv(24,time)
print(f"필요한 컴퓨터 : {result:.0f} ")


# 780달러와 650유로 노트북 중
# 달러로 구매했을때와 유로로 구매했을때
# 어느 것이 더 싼지 알아보세요
# 단, 2023.12.22 기준 환율을 적용하세요

import operator

usd = 1_299.00 * 780
euro = 1_428.77 * 650

cheaper = '더 싼 제품은 650유로 노트북 입니다.' if operator.gt(usd,euro): else '더 싼 제품은 780달러 노트북 입니다.'
print(f'{cheaper}')
