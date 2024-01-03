import sys
import json
from collections import OrderedDict
emps = {'response' :{'body':{'totalCount': 0, 'items': []}}}
def load_employees():
    print('프로그램을 초기화합니다...')
    global emps
    try:
        with open('employees.json','f',encoding=False) as f:
            emps = json.load(f)
    except:
        pass

    print('프로그램이 성공적으로 초기화 되었습니다')

def show_menu():
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


def input_employee():
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

def save_employee(emp):
    emps['response']['body']['items'].append(emp)
    emps['response']['body']['totalCount'] += 1
    with open('employees.json','w') as f:
        json.dump(emps,f,ensure_ascii=False)



def add_employee():
    print('사원 정보를 등록합니다.')
    emp = input_employee()
    save_employee(emp)




def read_employee():
    print('모든 사원의 정보를 조회합니다.')
    result = ''
    for emp in emps['response']['body']['items']:
        result += f"{emp['empno']}\t{emp['fname']}\t{emp['jobid']}\t{emp['deptid']}"

    print(result)
def readone_employee():
    print('특성 사원의 상세 정보를 조회합니다.')



def modify_employee():
    print('특성 사원의 정보를 수정합니다.')



def remove_employee():
    print('특성 사원의 정보를 제거합니다.')



def exit_program():
    print('프로그램을 종료합니다.')
    sys.exit(0)