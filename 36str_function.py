# 문자열 처리 함수들

ss = '파이썬' + '최고'
ss
ss = '파이썬' * 3
ss

# len() 함수 : 리스트나 문자열의 개수를 셀 때 사용
ss = 'abcefg'
len(ss)

ss = 'Python is Easy.  그래서 programming이 재밌습니다^^'
ss.upper()  # 모두 대문자
ss.lower()  # 모두 소문자
ss.swapcase() # 대/소 바꿈
ss.title() # 앞글자만 대문자

ss = '파이썬 공부는 즐겁습니다. 물론 모든 공부가 다 재미있진 않죠'
ss.count('공부') # 글자의 갯수 세기
ss.find('공부') # 글자의 위치 찾기
ss.rfind('공부') # 글자의 위치를 오른쪽부터 찾기
ss.find('공부',2) # 글자를 시작위치부터 찾기
ss.index('공부')
ss.rindex('공부')
ss.index('공부',5)

ss.startswith('파이썬')  # 시작하는 여부
ss.startswith('공부')
ss.endswith('공부') # 끝나는 여부

ss= '   파   이   썬   '
ss.strip() # 좌우 공백제거
ss.rstrip() # 우측 공백제거
ss.lstrip() # 좌측 공백제거

ss = '열심히 파이썬 공부 중 ~~'
ss.replace('파이썬','Python') # 문자열 변경

ss = 'Python을 열심히 공부 중'
ss.split() # 공백마다 분리
ss = '1:2:3'
ss.split(':') # :마다 분리해서 리스트화

before = ['2019', '12', '31']
after = list(map(int,before)) # 함수명에 대입
after

ss = '파이썬'
ss.center(10) # 문자열 정렬하기
ss.center(10,'-') # 문자열 정렬하기
ss.ljust(10)
ss.rjust(10)
ss.zfill(10) # 0으로 채우고 정렬

#문자열 파악하기

'1234'.isdigit()
'abcd'.isalpha()
'abc123'.isalnum()
'abcd'.islower()
'ABCD'.isupper()
' '.isspace()

