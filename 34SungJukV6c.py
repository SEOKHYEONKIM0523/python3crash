# 성적처리 프로그램 V6
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균, 학점을 계산하고 출력함
# 학점 기준 : 수우미양가
# 성적 입력, 조회, 상세 조회, 수정, 삭제 기능 구현
# 각 기능은 메뉴식으로 구현 - 기능별 메뉴 선택 시 명령 수행
# 성적 데이터를 json 자료구조로 구현
# 성적 처리 기능을 함수로 구현
# 성적 데이터는 파일 형태(sungjuk.json)로 저장
# 저장 양식은 '이름,국어,영어,수학,총점,평균,학점' 형태로 한다
# 파일 입출력 작업은 필요할 때만 사용하도록 수정

import poppo.sjv6c as sjv6

sjv6.load_sungjuk()

while True:
    # 프로그램 주 실행부
    menu = sjv6.show_menu()

    # 메뉴 선택에 따라 해당 기능 수행
    if menu == '1': sjv6.addsungJuk()
    elif menu == '2': sjv6.show_sungjuk()
    elif menu == '3': sjv6.showone_sungjuk()
    elif menu == '4': sjv6.modify_sungjuk()
    elif menu == '5': sjv6.remove_sungjuk()
    elif menu == '0':sjv6.exit_program()
    else:
        print('메뉴를 잘못 선택하셨습니다')






