# 성적처리 프로그램 v2
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균을 계산하고 출력함
# 단, 리스트를 이용해서 학생 3명에 대해 성적처리를 진행함
# 반복문을 이용하면 코드를 간단히 작성 가능
# 데이터 입력 시 input 함수 이용
names= input("학생 이름을 입력하세요")
kors = int(input("국어 점수를 입력하세요."))
engs = int(input("영어 점수를 입력하세요."))
mats = int(input("수학 점수를 입력하세요."))



names = []
kors = []
engs = []
mats = []
tots = []
avgs = []

# 성적 데이터 입력
for i in range(3):
    print(f'{i+1}번째 학생 데이터 입력')
    names.append(input('이름은 ? : '))
    kors.append(int(input('국어 점수는 ? : ')))
    engs.append(int(input('영어 점수는 ? : ')))
    mats.append(int(input('수학 점수는 ? : ')))


# 성적 처리
for i in range(len(names)):
    tots.append(kors[i] + engs[i] + mats[i])
    avgs.append(tots[i] / 3)


# 결과 출력
for i in range(len(names)):
    print(f'이름 : {names[i]}, 국어: {kors[i]}, 영어: {engs[i]}, 수학: {mats[i]}')
    print(f'총점: {tots[i]}, 평균: {avgs[i]:.1f}')

# 반복 수행 시 이터러블 객체가 필요없는 경우 변수명 대신 _ 를 사용
for _ in range(10):
    print('Hello, World!!')

