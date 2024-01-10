# 도서 관리 프로그램
# 도서명, 저자, 역자, 출판사, 출간일, 정가, 판매가, 할인율, 적립금
# bkname, author, publisher, pubdate, 
# retail, price, pctoff, mileage 
# 성적 데이터는 데이터베이스 테이블에 저장
# 클래스 기반으로 재작성
from poppo.BookService import BookService as bksrv
# BookService를 클래스로 변경했기 때문에
# from ~ import 구문으로 바꿔 객체 사용

while True:
    # 프로그램 주 실행부
    menu = bksrv.show_menu()

    # 메뉴 선택에 따라 해당 기능 수행
    if menu == '1': bksrv.new_book()
    elif menu == '2': bksrv.read_book()
    elif menu == '3': bksrv.readone_book()
    elif menu == '4': bksrv.modify_book()
    elif menu == '5': bksrv.remove_book()
    elif menu == '0':bksrv.exit_program()
    else:
        print('메뉴를 잘못 선택하셨습니다')






