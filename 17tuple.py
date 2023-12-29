# 튜플 자료형
# 순차적 데이터를 관리하는 자료형(순서가 존재)
# 리스트와 동일하지만, 변경 불가능 특성을 지님
# => 생성은 가능 / 추가,수정,삭제는 불가능
# 튜플 객체 생성은 ()를 사용

tuple1 = () # 빈 튜플
tuple2 = (1, 2, 3, 4, 5)
tuple3 = ('a', 'b', 'c', 'd', 'e')
tuple4 = (1, 'b', 3.14, 'd', 5)

print(tuple4)

# 튜플 추가/수정/삭제 해보기 - 불가능
tuple1.append(10)
tuple2[4] = 10
tuple2.pop()
tuple2.remove(3)

# 튜플 합치기 : +만 지원, extend 불가
print(tuple2 + tuple3)
tuple2.extend(tuple3)

# 만약, 튜플의 요소를 변경해야 한다면?
# 튜플을 리스트로 변환한 후 요소를 변경하고
# 다시 리스트를 튜플로 변환하면 됨
# 튜플을 리스트로 변환 : list(대상)
# 리스트를 튜플로 변환 : tuple(대상)

tuple1 = list(tuple1)
tuple1.append('A')
tuple1.append('B')
tuple1 = tuple(tuple1)
print(tuple1)

#리스트/튜플의 요소 인덱스 알아내기
tuple4.index(3.14)
tuple4.index('b')

numbers = (10, 20, 30, 40, 50, 60)
print(numbers[1:3])
print(numbers[0:2])
print(numbers[1:4])
print(numbers[3:len(numbers)-1])


# 난수 생성하기
# random이라는 모듈이 필요
# random()    : 0~1사이 임의의 부동소수점 숫자 출력
# randint(x,y) : x~y사이 임의의 정수 출력
# randrange(s,e,l) : 시작부터 끝 사이 임의의 출력
import random as rnd
rnd.seed(2312271045)
print(rnd.random())
print(rnd.randint(1, 10)) # 1 ~ 10 사이 난수 생성
print(rnd.randrange(1, 10)) # 1 ~ 9 사이 난수 생성

# 1 ~ 100사이의 임의의 3의 배수 출력
print(rnd.randrange(3,100+1,3))

# 1 ~ 45 사이 임의의 정수 6개를 추출해서
# 리스트와 튜플에 저장하는 코드를 작성하세요
import random as rnd
rnd.seed(2312271045)
print(rnd.random())
rand1 = []
rand2 = []
for _ in range(1,6+1):
    rand1.append(rnd.randint(1,45))
    rand2.append(rnd.randint(1,45))
print(rand1)
rand2=tuple(rand2)
print(rand2)

# 1 ~ 45 사이 임의의 정수 6개를 추출해서
# 리스트와 튜플에 저장하는 코드를 작성하세요
# 중복된 값은 제외
print(rnd.random())
rand1 = []
rand2 = []
for _ in range(1,6+1):
    rand1.append(rnd.randint(1,45))
    rand2.append(rnd.randint(1,45))
    if set in rand1 or set in rand2:
        rand1.clear()
        rand2.clear()
        rand1.append(rnd.randint(1, 45))
        rand2.append(rnd.randint(1, 45))
print(rand1)
rand2=tuple(rand2)
print(rand2)

lottos = []
cnt = 0
while len(lottos) < 6:
    cnt += 1
    lotto = rnd.randint(1,45)
    if lotto not in lottos:
        lottos.append(lotto)

print(lottos,cnt)

