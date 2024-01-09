import sys
from poppo.SungJuk import SungJuk
from poppo.SungJukService import SungJukService
from poppo.SungJukDAO import SungJukDAO


# 메뉴 출력
def show_menu():
    """
    선택할 프로그램을 고르는 함수
    :param: 없음
    :return: 처리할 함수를 고를 메뉴
    """

    main_menu = '''
    성적처리 프로그램 V8
    -----------------
    1. 성적 데이터 추가
    2. 성적 데이터 조회
    3. 성적 데이터 상세 조회
    4. 성적 데이터 수정
    5. 성적 데이터 삭제
    0. 프로그램 종료
    -----------------
    '''
    print(main_menu, end = '')
    menu = input('=> 메뉴를 선택하세요 : ')
    return menu


# 성적 데이터 입력
def read_sungjuk():
    """

    이름과 성적을 입력하는 함수
    :param: 없음
    :return: 성적 데이터
    """
    sungjuk = input('이름과 성적을 입력하세요 (예 : 홍길동 99 98 99)')
    data = sungjuk.split()

    name = data[0]
    kor = int(data[1])
    eng = int(data[2])
    mat = int(data[3])
    sj = [name,kor,eng,mat] # 입력받은 성적데이터를 리스트에 담음

    return sj


# 성적 처리 (총점/평균/학점 계산)
def compute_sungjuk(sj):
    """

    성적 데이터를 이용해 총점과 평균 학점을 구하는 함수
    :param sj: 기존에 저장된 성적 데이터
    :return: 성적처리된 성적데이터
    """
    tot = sj[1] + sj[2] + sj[3]
    avg = float(f"{tot / 3:.1f}")


    grd = '수' if avg >= 90 else \
        '우' if avg >= 80 else \
        '미' if avg >= 70 else \
        '양' if avg >= 60 else '가'

    return [sj[0], sj[1], sj[2], sj[3], tot, avg, grd]


# 성적 데이터 추가 (입력-처리-저장)
def addsungJuk():
    """
    성적 데이터를 추가하고 파일에 저장하는 함수
    :param: 없음
    :return: 없음
    """
    print('성적 데이터 추가')
    sj = SungJukService.read_sungjuk()
    SungJukService.compute_sungjuk(sj)

    rowcnt = SungJukDAO.insert_sungjuk(sj)

    print(f'{rowcnt} 건의 성적데이터가 추가됨')

# 모든 성적 데이터 출력 (번호/이름/국어/영어/수학/등록일)
def show_sungjuk():
    """

    모든 성적 데이터 출력(번호/이름/국어/영어/수학/등록일)
    :param: 없음
    :return: 없음
    """
    print('성적 데이터 조회')
    rows = SungJukDAO.select_sungjuk()
    for row in rows:
        print(f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {str(row[5])[10]}')


# 성적 데이터 상세 조회
def showone_sungjuk():
    """
    성적 데이터를 상세하게 보는 함수
    :param: 없음
    :return: 없음
    """
    sjno = input('상세 조회할 학생 번호는? ')

    row = SungJukDAO.selectone_sungjuk(sjno)

    print(f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}'
          f'{row[5]} {row[6]} {row[7]} {row[8]}')


# 성적 데이터 수정
def modify_sungjuk():
    """
    성적 데이터를 수정하는 함수
    :param: 없음
    :return: 없음
    """
    sjno = input('수정할 학생 번호는?')
    # 튜플 객체를 수정하기 위해 리스트 객체로 변환
    sj = list(SungJukDAO.selectone_sungjuk(sjno))

    if sj[0]: # 만일, 수정할 데이터가 존재한다면
        sj[1] = input(f'새로운 이름은? ({sj[1]}) : ')
        sj[2] = int(input(f'새로운 국어는? ({sj[2]}) : '))
        sj[3] = int(input(f'새로운 영어는? ({sj[3]}) : '))
        sj[4] = int(input(f'새로운 수학는? ({sj[4]})  : '))
        # 조회한 결과를 클래스 타입으로 변경 후 다시 성적 처리
        sj = SungJuk(sj[1], sj[2], sj[3], sj[4])
        SungJukService.compute_sungjuk(sj)

        rowcnt = SungJukDAO.update_sungjuk(sj,sjno)
        print(f'{rowcnt} 건의 데이터가 수정되었습니다.')

    else:
        print('데이터가 존재하지 않습니다')


# 성적 데이터 삭제
def remove_sungjuk():
    """
    성적 데이터를 삭제하는 함수
    :param: 없음
    :return: 없음
    """
    sjno = input('삭제할 학생 번호는?')

    rowcnt = SungJukDAO.delete_sungjuk(sjno)
    print(f'{rowcnt} 건의 데이터가 수정되었습니다.')
# 성적 처리 프로그램 종료
def exit_program():
    """

    성적처리 프로그램 종료 함수
    :param: 없음
    :return: 없음
    """
    print('프로그램 종료!')
    sys.exit(0)
