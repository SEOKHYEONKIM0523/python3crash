import os
import sys
from poppo.Book import Book
from poppo.BookDAO import BookDAO

# 클래스의 메서드 접근제한자
# public : 어느 클래스든지 모두 접근 가능
# protected : 상속 관계에 있는 클래스만 접근 가능(파이썬 지원x)
# default :  같은 패키지 내 클래스들끼리 접근 가능 ( 파이썬 지원x)
# private : 메서드를 정의한 클래스만 접근 가능 (메서드에 __ 추가)

class BookService:
    # 메뉴 출력
    @staticmethod
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


    @staticmethod
    def __input_book():
        try:
            bkname = input('도서명은?')
            author = input('저자는?')
            publisher = input('출판사는?')
            pubdate = input('출간일은?')
            retail = int(input('정가는?'))
            pctoff = int(input('할인율은?'))

            bk = Book(bkname,author,publisher,pubdate,retail,pctoff)
            bk.price = bk.retail * (1 - (bk.pctoff/100))
            bk.mileage = bk.retail * (bk.pctoff/100)

            return bk
        except:
            print('BookService - input_book에서 오류 발생 ')
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print('예외 내용 : ', exc_obj)
            print('예외 종류 : ', exc_type.__name__)
            print('예외 위치 : ', fname, exc_tb.tb_lineno)

    # 도서 데이터 추가 (입력-처리-저장)
    @staticmethod
    def new_book():
        """
        도서 데이터를 추가하고 파일에 저장하는 함수
        :param: 없음
        :return: 없음
        """
        print('도서 데이터 추가')
        try:
            bk = BookService.__input_book()

            rowcnt = BookDAO.insert_book(bk)
            print(f'{rowcnt} 건의 도서 데이터 등록됨!')
        except:
            print('BookService - new_book에서 오류 발생 ')
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print('예외 내용 : ', exc_obj)
            print('예외 종류 : ', exc_type.__name__)
            print('예외 위치 : ', fname, exc_tb.tb_lineno)

    # 모든 도서 데이터 출력
    @staticmethod
    def read_book():
        """
        모든 도서 데이터 출력(번호/도서명/저자/출판사/판매가)
        :param: 없음
        :return: 없음
        """
        rows = BookDAO.select_book()
        result = ''
        for row in rows:
            result += f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]:,}\n'
        print(result)

    # 도서 데이터 상세 조회
    @staticmethod
    def readone_book():
        """
        도서 데이터를 상세하게 보는 함수
        :param: 없음
        :return: 없음
        """
        bkname = input('상세 조회할 도서명은?')

        row = BookDAO.selectone_book(bkname)
        if row:
            print(f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}'
                  f'{row[5]:,} {row[6]:,} {row[7]}% {row[8]:,} {row[9]}')
        else:
            print('조회할 데이터가 없어요')

    @staticmethod
    def __reinput_book(obk):

        bkname = input(f'도서명은? ({obk[1]})')
        author = input(f'저자는? ({obk[2]})')
        publisher = input(f'출판사는? ({obk[3]})')
        pubdate = input(f'출간일은? ({obk[4]})')
        retail = int(input(f'정가는? ({obk[5]})'))
        pctoff = int(input(f'할인율은? ({obk[7]})'))

        bk = Book(bkname,author,publisher,pubdate,retail,pctoff)
        bk.price = bk.retail * (1 - (bk.pctoff/100))
        bk.mileage = bk.retail * (bk.pctoff/100)
        bk.bkno = obk[0]

        return bk


    # 도서 데이터 수정
    @staticmethod
    def modify_book():
        """
        도서 데이터를 수정하는 함수
        :param: 없음
        :return: 없음
        """
        bkname = input('수정할 도서이름는?')

        row = BookDAO.selectone_book(bkname)
        if row:
            bk = BookService.__reinput_book(row)
            rowcnt = BookDAO.update_book(bk)
            print(f'{rowcnt} 건의 데이터가 수정됨')

        else:
            print('수정할 데이터가 없어요')
    # 도서 데이터 삭제
    @staticmethod
    def remove_book():
        """
        도서 데이터를 삭제하는 함수
        :param: 없음
        :return: 없음
        """
        bkno = input('삭제할 도서 번호는?')
        rowcnt = BookDAO.delete_book(bkno)
        print(f'{rowcnt} 건의 도서 데이터 삭제됨!')


    # 도서 처리 프로그램 종료
    @staticmethod
    def exit_program():
        """

        도서처리 프로그램 종료 함수
        :param: 없음
        :return: 없음
        """
        print('프로그램 종료!')
        sys.exit(0)


