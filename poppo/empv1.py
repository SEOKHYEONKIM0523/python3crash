import sys
emps = []

def load_employees():
    print('프로그램을 초기화합니다...')
    global emps
    dicts = []

    with open('employees.csv') as f:
        datas = f.readlines()

        for data in datas:
            item = data.strip().split(',')
            d = {'empno':item[0], 'fname':item[1], 'lname':item[2], 'email':item[3],
                 'hdate':item[4], 'jobid':item[5], 'sal':item[6], 'deptid':item[7]}
            dicts.append(d)
        emps = dicts

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
    emp = {}

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
    row = (f"{emp['empno']}, {emp['fname']}, {emp['lname']}, {emp['email']}, "
           f"{emp['hdate']}, {emp['jobid']}, {emp['sal']}, {emp['deptid']}\n")
    with open('employees.csv','a') as f:
        f.write(row)
    emps.append(emp)



def add_employee():
    print('사원 정보를 등록합니다.')
    emp = input_employee()
    save_employee(emp)




def read_employee():
    print('모든 사원의 정보를 조회합니다.')
    result = ''
    for emp in emps:
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