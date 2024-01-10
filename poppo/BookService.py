import sys
from poppo.Book import Book
from poppo.BookDAO import BookDAO


# 메뉴 출력
def show_menu():
    """
    선택할 프로그램을 고르는 함수
    :param: 없음
    :return: 처리할 함수를 고를 메뉴
    """

    main_menu = '''
    -----------------
    도서관리 프로그램 V1
    -----------------
    1. 도서 데이터 추가
    2. 도서 데이터 조회
    3. 도서 데이터 상세 조회
    4. 도서 데이터 수정
    5. 도서 데이터 삭제
    0. 프로그램 종료
    -----------------
    '''
    print(main_menu, end = '')
    menu = input('=> 메뉴를 선택하세요 : ')
    return menu


# 도서 처리 (총점/평균/학점 계산)
def compute_book():
    """

    도서 데이터를 이용해 총점과 평균 학점을 구하는 함수
    :param : 기존에 저장된 도서 데이터
    :return: 도서처리된 도서데이터
    """
    pass


# 도서 데이터 추가 (입력-처리-저장)
def new_book():
    """
    도서 데이터를 추가하고 파일에 저장하는 함수
    :param: 없음
    :return: 없음
    """
    pass
# 모든 도서 데이터 출력
def read_book():
    """
    모든 도서 데이터 출력(번호/도서명/저자/출판사/판매가)
    :param: 없음
    :return: 없음
    """
    pass

# 도서 데이터 상세 조회
def readone_book():
    """
    도서 데이터를 상세하게 보는 함수
    :param: 없음
    :return: 없음
    """
    bkname = input('상세 조회할 도서명은?')
    pass

# 도서 데이터 수정
def modify_book():
    """
    도서 데이터를 수정하는 함수
    :param: 없음
    :return: 없음
    """
    bkno = input('수정할 도서번호는?')
    pass

# 도서 데이터 삭제
def remove_book():
    """
    도서 데이터를 삭제하는 함수
    :param: 없음
    :return: 없음
    """
    bkno = input('삭제할 도서 번호는?')
    pass
# 도서 처리 프로그램 종료
def exit_program():
    """

    도서처리 프로그램 종료 함수
    :param: 없음
    :return: 없음
    """
    print('프로그램 종료!')
    sys.exit(0)
