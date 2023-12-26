# 슬라이싱
# 연속적인 객체들(리스트,튜플,문자열)에 범위를 지정하고
# 선택해서 부분적으로 객체를 가져오는 방법 및 표기법
# 리스트 객체에서 필요한 부분의 항목만 뽑아 사용하는 것
# 객체명[시작:끝-1:스텝]

# 다음 코드에서 생년월일 추출
jumin = '123456-1234567'
print(jumin[:6]) #시작을 생략하면 리스트의 인덱스는 0부터

# 생년월일과 - 를 제외한 나머지 추출
print(jumin[7:]) # 끝을 생략하면 리스트의 맨 마지막 문자까지 출력

# 코드에서 짝수/홀수 위치의 문자 추출
print(jumin[0::2]) # 홀수 위치
print(jumin[1::2]) # 짝수 위치

# 역순으로 추출 : step을 -로 설정
print(jumin[14::-1])
print(jumin[::-1])

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#역순
print(alphabet[::-1])
#인덱스 2~5
print(alphabet[2:6])
print(alphabet[0:5])
print(alphabet[3:8])
print(alphabet[5:])
print(alphabet[3:9])


cardnum = int(input('카드번호는?: '))

if cardnum[:2] == '35':
    if cardnum == 356317: cardname = 'JCB카드 NH농협카드'
    elif cardnum == 356901: cardname = 'JCB카드 신한카드'
    elif cardnum == 356912: cardname = 'JCD카드 KB국민카드'
elif cardnum[:1] == '4':
    if cardnum == 404825: cardname = '비자카드 NH농협카드'
    elif cardnum == 438676: cardname = '비자카드 신한카드'
    elif cardnum == 457973: cardname = '비자카드 KB국민카드'
if cardnum[:1] == '5':
    if cardnum == 515594: cardname = '마스타카드 NH농협카드'
    elif cardnum == 524353: cardname = '마스타카드 신한카드'
    elif cardnum == 540926: cardname = '마스타카드 KB국민카드'

print(f'{cardnum} {cardname}')

# 리스트 합치기 : extend, +
a = [1, 2, 3]
b = [4, 5, 6]
c = [ '7', '8', '9']

a.extend(b)
a = a + b
b.extend(c)
b
#리스트의 특정 요소 존재 파악: in
todo = ['cleaning', 'shopping', 'study', 'exercise','game']
print('shopping' not in todo)
#리스트의 모든 요소 존재 순회 (in, not in)
for item in todo:
    print(item,end=' ')
#리스트의 모든 요소 존재 순회 : enumerate (항목의 인덱스도 출력)
for idx, item in enumerate(todo):
    print(idx, item)

#리스트의 모든 요소 제거 : clear
print(todo)
todo.clear()



blood = []
A=0
B=0
AB=0
O=0
for i in range(1,11):
     blood.insert(i-1,input(f"헌혈해 주셔서 감사합니다. 혈액형을 선택하세요 {i}/10\n"
              "A, B, AB, O : "))
     print(blood)

for bd in blood:
    if bd == 'A': A += 1
    elif bd == 'B' : B += 1
    elif bd == 'AB' : AB += 1
    elif bd == 'O' : O += 1

print(f'''
----------------------
혈액형 : 개수
----------------------
A형 : {A}
B형 : {B}
AB형 : {AB}
O형 : {O}
-----------------------''')


# 리스트의 항목별 빈도 계산 : count (값)
blood.count('A')
blood.count('B')
blood.count('AB')
blood.count('O')


