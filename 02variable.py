# 변수

# 어떠한 값을 저장하는 장소를 기억하기 쉽게 문자형태로 나타낸 것
# 변수에 값이 저장되는 공간을 메모리라 함
# 변수에 값을 넣으라고 선언하면,
# 시스템상의 메모리 어딘가에 공간을 확보하고
# 그 공간의 실제주소와 이름을 매핑함

#이름과 나이를 저장하는 변수

a = '홍길동'
b = 99

name = '홍길동' #의미있는 단어로 변수 선언
age = 99

# 변수명은 대소문자 구분
Name = '일지매'
# 변수에 저장된 값을 출력하려면 print 함수 사용
print(name, age)
print(Name, age)


# 파이썬의 자료형(data-type)
# 정적 타입 : 변수 선언시 자료형도 같이 표시
#            (String name = "홍길동")
#            (name = 123) (오류발생-선언시 자료형과 값의 유형이 다름)

# 동적 타입 : 변수 선언시 자료형은 생략 가능, 추론기능으로 자동할당,
#            또한, 변수에 대입하는 값에 따라 자료형이 바뀜
#            (name = '홍길동')
#            (name = 123) (문제없음-변수의 자료형은 자동으로 변경)



# 변수의 자료형을 알아보기 위해 type 함수 사용
print(type(name))

name = 123 #동적 자료형 변환 시험
print(type(name))

# ex) 회원정보 저장용 변수 선언
# 아이디, 비번, 이름, 나이, 이메일,
# 결혼여부, 보유금액, 등록일

userid = 'ooooop'
passwd = '123123'
name = '김석현'
age = 27
email = 'aasbc@gmail.com'
isMarried = True
ownmoney= 10000
regdate = '2023-12-19 16:15:35'

#파이썬 자료형 - 정수, 실수, 문자, boolean
# 정수 자료형 - 소숫점 이하의 값이 없는 수
int1 = 123
int2 = 0b01010101 #2진수

print(int1, int2, bin(int2))

# 실수 자료형 - 소수점 이하의 값이 있는 수
# 부동소수점 floating point 실수 : 국제 표준에 따라 실수를 표기하는 방법
#즉, 실수를 정수부와 정수의 곱으로 된 지수로 표현하는 것
# 예) 123.456 => 123456 x 10^(-3)
float1 = 10.0
float2 = 123456e-3
print(float1, float2)

# 부동소수점과 오차
# 컴퓨터에서 숫자는 비트를 이용해서 표현하기 때문에
# 실수는 정확하게 나타낼 수 없음! - 단지 근삿값으로만 표현
# 0.1 + 0.2 == 0.3

round(0.1 + 0.2, 5) == round(0.3, 5)


# 문자 자료형
#파이썬에서 글자 char 를 문자열 string 이라 표현
# 문자열은 ''나 ""를 이용해서 정의 가능 - '' 추천
# 여러줄 문자열(텍스트)를 작성할 때는 ''' ''' 를 사용
str1 = 'Hello, World'
str2 = 'Hello, \nWorld!!'
str3 = 'Hello, \
world!!'
str4 = '''Hello,
world!!
'''
print(str1)
print(str2)
print(str3)
print(str4)

# boolean 자료형
#참, 거짓을 나타내는 자료형
#True, False 등으로 표현
#한편, 숫자가 0이거나 빈 문자열이면 False로 표현
bool1 = True
bool2 = False
bool3 = 0


print(bool1, bool2)

# 유효숫자e지수 표현법으로 되어 있는 다음 숫자를 보통의 소숫점 표현으로 나타내라.
# 5e8
5.0 x 100000000
# 5.6e3
5.6 x 1000
# -2.1e2
-2.1 x 100
# -3.4e-1
-3.4 x 0.1
# 다음 숫자를 유효숫자e지수 표현법으로 나타내라. 유효숫자는 정수가 되어야 한다.
# 3.141592
314e4
a=3141592e-7
a=float(3141592e-6)
print(a)

# 2.718
2718e-3
a=float(2718e-3)
print(a)
# 1.4
14e-1
# 1.73
173e-2

fruit = 'apple22'
print (fruit)

first_name = 'ada'
last_name = 'lovelace'
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello,{full_name}")