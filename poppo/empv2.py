import sys
import json
from collections import OrderedDict
emps = {'response' :{'body':{'totalCount': 0, 'items': []}}}
items = []


# 메뉴 출력
def show_menu():
    """
    선택할 프로그램을 고르는 함수
    :param: 없음
    :return: 처리할 함수를 고를 메뉴
    """

    main_menu = '''
    사원관리 프로그램 V1
    -----------------
    1. 사원 정보 추가
    2. 사원 정보 조회
    3. 사원 정보 상세 조회
    4. 사원 정보 수정
    5. 사원 정보 삭제
    0. 프로그램 종료
    -----------------
    '''
    print(main_menu, end='')
    menu = input('=> 메뉴를 선택하세요 : ')
    return menu


# 사원 데이터 입력
def input_employee():
    """

    사원의 정보를 입력하는 함수
    :param: 없음
    :return: 사원 데이터
    """
    emp = OrderedDict()

    emp['empno'] = input('사원 번호를 입력하시오. ')
    emp['fname'] = input('이름을 입력하시오. ')
    emp['lname'] = input('성을 입력하시오. ')
    emp['email'] = input('이메일을 입력하시오. ')
    emp['hdate'] = input('입사일을 입력하시오. ')
    emp['jobid'] = input('직책을 입력하시오. ')
    emp['sal'] = input('급여를 입력하시오. ')
    emp['deptid'] = input('부서번호를 입력하시오. ')

    return emp


# 사원 데이터 저장 (employees.json 파일)
def save_employee(emp):
    """
    입력한 성적 데이터를 파일로 저장하는 함수
    :param sj: 기존에 저장된 성적데이터
    :return: 없음
    """
    items.append(emp)
    emps['response']['body']['totalCount'] += 1
    with open('employees.json','w') as f:
        json.dump(emps,f,ensure_ascii=False)


# 사원 데이터 추가 (입력-처리-저장)
def add_employee():
    """
    사원 데이터를 추가하고 파일에 저장하는 함수
    :param: 없음
    :return: 없음
    """
    print('사원 정보를 등록합니다.')
    emp = input_employee()
    save_employee(emp)


# 프로그램 시작 시 employees.jason 파일을 읽어 emps 변수에 초기화
def load_employees():
    """
    성적 데이터를 읽는 함수
    :param: 없음
    :return: 없음
    """
    global emps,items

    print('프로그램을 초기화합니다...')

    try:
        with open('employees.json') as f:
            emps = json.load(f)
            items = emps['response']['body']['items']
    except:
            items = emps['response']['body']['items']


    print('프로그램이 성공적으로 초기화 되었습니다')


# 모든 사원 데이터 출력(사번,이름,직업번호,부서번호)
def read_employee():
    """

    성적 데이터 수정 시 수정할 데이터 입력 받는 함수
    :param: 없음
    :return: 없음
    """
    print('모든 사원의 정보를 조회합니다.')
    result = ''
    for emp in emps['response']['body']['items']:
        result += f"{emp['empno']}\t{emp['fname']}\t{emp['jobid']}\t{emp['deptid']}"

    print(result)


# 사원 데이터 상세 조회
def readone_employee():
    """
    사원 데이터를 상세하게 보는 함수
    :param: 없음
    :return: 없음
    """
    print('특성 사원의 상세 정보를 조회합니다.')
    empno = input('상세 조회할 사원의 사번은? ')
    info = '찾는 데이터가 없습니다'

    for emp in emps['response']['body']['items']:
        if emp['empno'] == empno:
            info = (f"{emp['empno']} {emp['fname']} {emp['lname']} {emp['email']}"
                    f"{emp['hdate']} {emp['jobid']} {emp['sal']} {emp['deptid']}")
            break

    print(info)

# 사원 데이터 수정 시 수정할 데이터 입력받기
def read_again(data, empno):
    """

    사원 데이터 수정 시 수정할 데이터 입력 받는 함수
    :param data: 기존에 저장된 사원 데이터
    :param empno: 수정할 데이터의 사번
    :return: 새롭게 생성된 사번데이터
    """
    empno = empno
    fname = input(f"새로운 이름은? ({data['fname']}) : ")
    lname = input(f"새로운 성은? ({data['lname']}) : ")
    email = input(f"새로운 이메일은? ({data['email']}) : ")
    hdate = input(f"새로운 입사일은? ({data['hdate']}) : ")
    jobid = input(f"새로운 직업번호는? ({data['jobid']}) : ")
    sal = input(f"새로운 급여는? ({data['sal']}) : ")
    deptid = input(f"새로운 부서번호는? ({data['deptid']}) : ")

    data = OrderedDict()
    data['empno'] = empno
    data['fname'] = fname
    data['lname'] = lname
    data['email'] = email
    data['hdate'] = hdate
    data['jobid'] = jobid
    data['sal'] = sal
    data['deptid'] = deptid

    return data


# 사원 데이터 수정/삭제한 내용 반영
def flush_employees():
    """
    성적 데이터를 반영하는 함수
    :param: 없음
    :return: 없음
    """
    with open('employees.json', 'w',encoding='utf8') as f:
        json.dump(emps, f, ensure_ascii=False)


# 사원 데이터 수정
def modify_employee():
    """
    성적 데이터를 수정하는 함수
    :param: 없음
    :return: 없음
    """
    print('특성 사원의 정보를 수정합니다.')

    empno = input('수정할 사원의 사번은?')

    data = None
    idx = None
    for i, emp in enumerate(items):
        if emp['empno'] == empno:
            data = emp
            idx = i

    if data:
        data = read_again(data,empno)

    #리스트에 기존 데이터를 버리고 새로운 데이터로 재설정
        items[idx] = data

    #변경 사항을 json 파일에 반영
        flush_employees()

    else:
        print('찾는 데이터가 없습니다!')


# 사원 데이터 삭제
def remove_employee():
    """
    사원 데이터를 삭제하는 함수
    :param: 없음
    :return: 없음
    """
    print('특성 사원의 정보를 제거합니다.')

    empno = int(input('삭제할 사원의 사번은?'))

    # 삭제할 데이터를 찾음
    data = None
    for emp in items:
        if emp['empno'] == empno:
            data = emp
            break
    # 삭제할 데이터를 찾았다면
    if data:
        confirm = input('정말로 삭제하시겠습니까? (yes/no)')
        if confirm == 'yes':
            items.remove(data)
            emps['response']['body']['totalCount'] -= 1
            print(f'{empno}의 데이터가 삭제되었습니다')
            flush_employees()
        else:
            print('삭제가 취소되었습니다')




# 사원 정보 프로그램 종료
def exit_program():
    '''
    사원 정보 프로그램 종료 함수
    :param: 없음
    :return: 없음
    '''
    print('프로그램을 종료합니다.')
    sys.exit(0)