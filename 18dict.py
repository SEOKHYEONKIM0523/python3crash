# 딕서너리
# 이름key과 값value으로 구성된 연관배열의 일종
# 자료구조 만들때 {}를 사용하고
# 이름과 값은 : 으로 구분해서 정의함
# 다른 언어의 JSON과 유사한 구조
# 데이터분석시 주로 사용하는 자료구조 : mongodb
# 키를 통해 자료를 찾는 해쉬테이블을 이용하므로 검색속도가 빠름

# 중간고사 성적을 dict로 선언
mids = { 'C/C++': 'a', 'Java': 'B+', '네트워킹': 'C',
         '보안': 'A+', '해킹': 'F', '시스템': 'C+'}
print(mids)

# 회원 정보를 dict로 선언
# key: 이름, 아이디, 비번, 이메일, 주소, 성적(국영수)
member = { '이름': '홍길동', '아이디': 'Gildong', "비번": 'passwd','이메일': 'abc123@xyz.co.kr',
           '주소': '서울시 관악구', '성적': [90,90,70]}
print(member)

# 딕셔너리 다루기
# 조회 : 변수명[키], 변수명.get(키)
print(member['이름'])
print(member['성적'][0])

print(member.get('이름'))
print(member.get('성적')[1])

# 존재하지 않는 키 지정 시
member['zipcode']     # 오류
member.get('zipcode') # none

# 새로운 항목 추가 : 변수명[새로운키] = 새로운 값
member['zipcode'] = '12345'
print(member)

# 기존 항목 변경 : 변수명[키] = 변경할값
member['zipcode'] = '98765'
member['주소'] = '서울시 광진구 자양동'

# 기존 항목 삭제 : del 변수명[키], 변수명.pop(키)
del member['zipcode']
member.pop('주소')
#존재하지 않는 키 삭제 시
del member['blood'] #오류 발생
member.pop('blood') #오류 발생
member.pop('blood', None)

# 항목 수 조회 : len
print(len(member))

# dict의 모든 키/값 조회 :keys, values
print(member.keys())
print(member.values())

# dict 전체 항목 출력
# 출력 형식은 '키 = 값'
for key in member.keys():
    print(f'{key} = {member[key]}')

# 중간고사 성적 관리 프로그램 만들기
#1
exam = { 'C/C++': 'A', 'Java': 'B+', '모바일': 'C',
         '보안': 'A+', '해킹': 'F', '시스템': 'C+'}
#2
exam['Java']
exam['시스템']
#3
exam["파이썬"] = 'A'
exam["OS"] = 'A+'
#4
exam['Java'] = 'F'
exam['시스템'] = 'A'
exam
#5
for key in exam.keys():
    print(f'{key} = {exam[key]}')

# 수학 시험 프로그램

math = ('3+2', '5/2의 몫', '10-2', '10^2*2', '1-(10%4의 나머지)', '2^4', '4/2')
i=-1
right =0
score=0
while i<=5:
    i += 1
    answer = int(input(f'문제 : {math[i]} \n'
                   f'정답을 입력하세요. '))
    if i==0 and answer == 5:
        score +=3
        right +=1
    elif i == 1 and answer == 2:
        score += 5
        right += 1
    elif i == 2 and answer == 8:
        score += 3
        right += 1
    elif i == 3 and answer == 200:
        score += 5
        right += 1
    elif i == 4 and answer == -1:
        score += 5
        right += 1
    elif i == 5 and answer == 16:
        score += 3
        right += 1
    elif i == 6 and answer == 2:
        score += 3
        right += 1
print(f'''
-------------------------
정답 개수: {right}
오답 개수: {7-right}
Total Score: {score}
-------------------------
''')


quizs = (('3+2는? (3점)', 5, 3), ('5÷2의 몫은? (5점)', 2, 5), ('10 - 2는? (3점)',8,3), ('10² x 2는? (5점)', 200,5),
         ('1-(10÷4의 나머지) (5점)', -1, 5), ('2⁴ (3점)', 16, 3), ('4÷2 (3점)', 2, 3))

trueCount = 0
falseCount = 0
totalScore = 0

for idx, q in enumerate (quizs):
    print(f'문제 {idx+1}/7 : ',q[0])
    answer = int(input('정답을 입력하세요 : '))

    if answer == q[1]:
        trueCount += 1
        totalScore += q[2]
    else: falseCount += 1

print(f'''
-------------------------
정답 개수: {trueCount}
오답 개수: {falseCount}
Total Score: {totalScore}
-------------------------
''')



# 회원가입 프로그램
signup = {}

i=0
while True:
    new = input('1.회원가입, 2.프로그램 종료 중 고르시오 : ')
    if new == '1':
        id=input('아이디를 입력하시오')
        passwd = input('비밀번호를 입력하시오')
        signup[f'{id}'] = passwd

    elif new == '2':
        print('프로그램이 종료되었습니다.')
        for key in signup.keys():
             print(f'{key} , {signup[key]}')
        break

# 회원가입 프로그램 V1
users = {}

while True:
    menu = int(input('1. 회원가입 2. 프로그램 종료'))

    if menu == 1:
        userid = input('아이디를 입력하세요.')
        passwd = input('비밀번호를 입력하세요.')
        users[userid] = passwd
    elif menu == 2:
        print('-------------------------')
        print('아이디: 비밀번호')
        print('-------------------------')
        for k in users.keys():
            print(f'{k} : {users[k]}')
        print('-------------------------')
        break
    else:
        print('잘못 입력하셨습니다.')

# 회원가입 프로그램 V2

users = {'response' :{'body':{'totalCount':999, 'items': []}}}
print(users['response']['body']['totalCount'])
print(users['response']['body']['items'])

print(users['response']['body']['items'].append({'uid':'abc', 'pwd' : '123'}))
print(users['response']['body']['items'].append({'uid':'xyz', 'pwd' : '987'}))
print(users['response']['body']['items'])

for item in users['response']['body']['items']:
    for key in item.keys():
        print(key, item[key])

while True:
    menu = int(input('1. 회원가입 2. 프로그램 종료'))

    if menu == 1:
        userid = input('아이디를 입력하세요.')
        passwd = input('비밀번호를 입력하세요.')
        user = {}
        user['userid'] = userid
        user['passwd'] = passwd
        users['response']['body']['items'].append(user)

    elif menu == 2:
        print('-------------------------')
        print('아이디: 비밀번호')
        print('-------------------------')
        for item in users['response']['body']['items']:
            for k in item.keys():
                print(f'{k}, {item[k]}')
        print('-------------------------')
        break
    else:
        print('잘못 입력하셨습니다.')

