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