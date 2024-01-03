# 사원 정보를 입력 받아 employees.csv 파일에 저장
# 저장된 사원 정보를 화면 출력
# 저장 시 :사번, 이름, 성, 이메일, 입사일, 직책, 급여, 부서번호
# 출력 시 : 사번, 이름, 직책, 부서번호

import poppo.empv1 as emp

emp.load_employees()

while True:
    menu = emp.show_menu()

    if menu == '1' : emp.add_employee()
    elif menu == '2' : emp.read_employee()
    elif menu == '3' : emp.readone_employee()
    elif menu == '4' : emp.modify_employee()
    elif menu == '5' : emp.remove_employee()
    elif menu == '0' : emp.exit_program()
    else: print('메뉴를 잘못 선택하셨습니다.')
