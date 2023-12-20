# 성적처리 프로그램 v1
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균을 계산하고 출력함

name='홍길동'
korean=43
english=30
math=85
total = korean + english + math
average = (korean + english + math)/3
print(f'{name:s}, 총점 = {total:d} , 평균 = {average:.1f}')
