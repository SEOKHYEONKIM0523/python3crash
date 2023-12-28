# 함수와 모듈
# 함수는 일정한 작업을 수행하는 코드 집합체
# 보통 반복적으로 사용되는 코드들을 함수로 정의해서 사용

# 즉, 반복적으로 사용할 가치가 있는 코드를 한 뭉치로 묶고
# (어떤 입력값을 주면) 결과가 반환되도록 사용

# 또한, 여러 코드들을 함수화하면 프로그램의 흐름을
# 일목요연하게 파악하기 쉬움

# 코드의 이식성이나 재사용성이 높아짐 - 개발 속도가 빨라짐

# 다른 사람과의 협업시 코드가 섞이지 않게 하기 위한
# 목적도 있음 - 모듈



print('선생님 미워요') # 단순출력

print('선생님 미워요') # 반복출력
print('선생님 미워요')
print('선생님 미워요')

for _ in range(3):
    print('선생님 미워요') # 개선된 반복

# 이러한 반복문을 여러번 사용해야 한다면?
# 만약 미워요 대신 싫어요나 좋아요로 바꿔야 한다면


# 함수 정의
# def 함수명(매개변수):
#     함수몸체(코드들)


def saymsg():
    for _ in range(3):
        print('선생님 미워요')

# 함수 호출
# 함수명(), 함수명(입력값)
saymsg()


def saymsg2():
    for _ in range(3):
        msg = '미워요'
        print(f'선생님 {msg}')

saymsg2()

def saymsg3(msg):
    for _ in range(3):
        print(f'선생님 {msg}')

saymsg3('미워요')



def sensorOn():
    print('온도센서 작동을 시작한다.')

def sensorOff():
    print('온도센서 작동을 중지한다.')

def notebookSize():
    length = float(input('길이를 입력하세요.(cm) '))
    print(f'{length} cm = {length / 2.54:.4f} inch')

notebookSize()


def climbing():
    MT = int(input('이동 시간을 입력하세요.'))
    MV = int(input('이동 거리를 입력하세요.'))
    print(f'이동거리는 {MT*MV:.1f} km 입니다')

climbing()

# 함수의 유형
# 입력값 x   반환값 x
# 입력값 x   반환값 o 자주씀   !!
# 입력값 o   반환값 x
# 입력값 o   반환값 o  자주씀  !!!
def saymsg4(msg): # 입력값 o, 처리 결과 반환 (반환값 o)
    text = ''
    for _ in range(3):
        text += f'선생님 {msg}\n'
    return text # 결과를 처리하지 않고 넘김
print(saymsg4('미워요'))


def notebookSize2():
    print('길이를 입력하세요.(cm) ', end = ' ')
    length = int(input())
    cm2inch = length * 0.393701
    return cm2inch

print(f'{notebookSize2():.1f} inch')
print(f'{notebookSize2():.1f} 인치')

def notebookSize3():
    print('길이를 입력하세요.(cm) ', end = ' ')
    length = int(input())
    cm2inch = length * 0.393701
    return length, cm2inch

length, cm2inch = notebookSize3()
print(f'{length} cm = {cm2inch:.4f} inch')
print(f'{length} 센티미터 = {cm2inch:.4f} 인치')


def movedist2():
    times = int(input('이동 시간을 입력하세요.'))
    speed = int(input('이동 거리를 입력하세요.'))
    dist = times * speed
    return dist

dist = movedist2()
print(f'이동거리는 {dist:.1f} km 입니다')

# 계산기 프로그램


num = int(input('숫자를 입력하세요. '))
cal = int(input('연산자를 선택하세요. 1.덧셈, 2.뺄셈, 3.곱셈, 4.나눗셈 '))
num2 = int(input('숫자를 입력하세요. '))
if cal == 1:
    result = num + num2
elif cal == 2:
    result = num - num2
elif cal == 3:
    result = num * num2
elif cal == 4:
    result = num / num2
print(f'곱셈 결과 : {result:.1f}')


def sum():
    result = num + num2

def dif():
    result = num - num2

def cro():
    result = num * num2

def dev():
    result = num / num2

def calculator():
    num = int(input('숫자를 입력하세요. '))
    cal = int(input('연산자를 선택하세요. 1.덧셈, 2.뺄셈, 3.곱셈, 4.나눗셈 '))
    num2 = int(input('숫자를 입력하세요. '))

    if cal == 1:
        result = num + num2
        cal = '덧셈'
    elif cal == 2:
        result = num - num2
        cal = '뺄셈'
    elif cal == 3:
        result = num * num2
        cal = '곱셈'
    elif cal == 4:
        result = num / num2
        cal = '나눗셈'
    return result

result = calculator()
print(f'{cal} 결과 : {result:.1f}')

# 프로그램 객체지향 설계 5원칙
# SOLID


# 계산기 프로그램
def readData():
    op1 = int(input('숫자를 입력하세요. '))
    op2 = input('연산자를 선택하세요. 1.덧셈, 2.뺄셈, 3.곱셈, 4.나눗셈 ')
    op3 = int(input('숫자를 입력하세요. '))
    return op1, op2, op3


def computeNumber(op1,op2,op3):
    result = 0
    if op2 == '1':
        result = op1 + op3
        op2 = '덧셈'
    elif op2 == '2':
        result = op1 - op3
        op2 = '뺄셈'
    elif op2 == '3':
        result = op1 * op3
        op2 = '곱셈'
    elif op2 == '4':
        result = op1 / op3
        op2 = '나눗셈'
    return op2, result
def computer():
    # 데이터 입력부
    op1, op2, op3 = readData()

    # 데이터 계산
    op2, result = computeNumber(op1,op2,op3)

    # 처리 결과 넘김
    return op2, result

op2, result = computer()
print(f'{op2} 결과 : {result:.1f}')


# 함수에 값 전달하기
# 매개변수 parameter : 함수 정의 시 함수에서 사용할 변수 정의
# 매개변수는 함수 호출 시 전달 받은 인수로 초기화되어 사용됨
# 인수 argument : 함수 호출 시 매개 변수에 전달할 실제 값



def insertData():
    length = int(input('길이(mm)를 입력하세요.'))
    unit = int(input('원하는 단위를 입력하세요 1.cm 2.m 3.inch 4.ft'))
    result = 0
    return length, unit, result


def resultData(length, unit, result):
    if unit == 1:
         result = length * 0.1
         unit = 'cm'
    elif unit == 2:
         result = length * 0.001
         unit = 'm'
    elif unit == 3:
         result = length * 0.03937
         unit = 'inch'
    elif unit == 4:
         result = length * 0.003281
         unit = 'ft'
    return result, unit


def convertUnit():
    length, unit, result = insertData()
    unit, result = resultData(length, unit, result)
    return length, unit, result


length, result, unit = convertUnit()
print(f'{length} mm --> {result} {unit}')



def insertData2():
    length = int(input('길이(mm)를 입력하세요.'))
    return length

def convertUnit2():
    length = insertData2()
    print(f'''
    {length} mm --> {length * 0.1} cm
    {length} mm --> {length * 0.001} m
    {length} mm --> {length * 0.03937} inch
    {length} mm --> {length * 0.003281} ft
    ''')
    return length

length = convertUnit2()




def readMM():
    mm = int(input('길이(mm)를 입력하세요.'))
    return mm


def convertAll(mm):
    cm = mm * 0.1
    m = mm * 0.001
    inch = mm * 0.03937
    ft = mm * 0.003281

    return cm, m, inch, ft

def convertUnit3():
    mm = readMM()

    cm, m, inch, ft = convertAll(mm)

    return cm, m, inch, ft,mm

cm, m, inch, ft, mm = convertUnit3()

print(f'''
{mm} mm --> {cm} cm
{mm} mm --> {m} m
{mm} mm --> {inch} inch
{mm} mm --> {ft} ft
 ''')