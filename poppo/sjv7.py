import sys
import oracledb
import json

# 데이터베이스 연결정보
host = ''
userid = ''
passwd = ''
sid = ''

dsn_tns = oracledb.makedsn(host,1521,sid)


# 메뉴 출력
def show_menu():
    """
    선택할 프로그램을 고르는 함수
    :param: 없음
    :return: 처리할 함수를 고를 메뉴
    """

    main_menu = '''
    성적처리 프로그램 V7
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


# 모든 성적 데이터 출력 (번호/이름/국어/영어/수학/등록일)
def show_sungjuk():
    """

    모든 성적 데이터 출력(번호/이름/국어/영어/수학/등록일)
    :param: 없음
    :return: 없음
    """
    print('성적 데이터 조회')
    sql = ('select sjno,name,kor,eng,mat,regdate from sungJuk '
           'order by sjno desc')

    conn = oracledb.connect(user=userid, password=passwd, dsn=dsn_tns)
    cursor = conn.cursor()

    cursor.execute(sql)


    for sjno, name, kor, eng, mat,regdate in cursor:
        print(sjno, name, kor, eng, mat,str(regdate)[:10])

    cursor.close()
    conn.close()


# 성적 데이터 저장 (sungjuk 테이블)
def save_sungjuk(sj):
    """
    입력한 성적 데이터를 파일로 저장하는 함수
    :param sj: 기존에 저장된 성적데이터
    :return: 없음
    """

    sql = ' insert into sungJuk (name, kor, eng, mat, tot, avg, grd) values (:1,:2,:3,:4,:5,:6,:7) '
            # values(?,?,?,?,?,?,?) <== 오라클에선 안됨
            # values(:name,:kor,:eng,:mat,:tot,:avg,:grd)  사용가능

    conn = oracledb.connect(user=userid, password=passwd, dsn=dsn_tns)
    cursor = conn.cursor()

    cursor.execute(sql,sj)
    conn.commit()

    print(cursor.rowcount, '건의 성적데이터 추가됨')

    cursor.close()
    conn.close()





# 성적 데이터 추가 (입력-처리-저장)
def addsungJuk():
    """
    성적 데이터를 추가하고 파일에 저장하는 함수
    :param: 없음
    :return: 없음
    """
    print('성적 데이터 추가')
    sj = read_sungjuk()
    sj = compute_sungjuk(sj)
    save_sungjuk(sj)  # 성적 데이터를 파일에 저장


# 프로그램 시작 시 sungjuks.jason 파일을 읽어 sjs 변수에 초기화
def load_sungjuk():
    """
    성적 데이터를 읽는 함수
    :param: 없음
    :return: 없음
    """
    global sjs,items,totalCount

    try:           # 작업 중에 오류가 발생하면
        with open('sungjuks.json',encoding='utf8') as f:
            sjs = json.load(f)
            items = sjs['response']['body']['items']
            totalCount = sjs['response']['body']['totalCount']
    except:
        items = sjs['response']['body']['items']
        totalCount = sjs['response']['body']['totalCount']


# 성적 데이터 상세 조회
def showone_sungjuk():
    """
    성적 데이터를 상세하게 보는 함수
    :param: 없음
    :return: 없음
    """
    sjno = input('상세 조회할 학생 번호는? ')
    info = '찾는 데이터가 없습니다'

    dsn_tns = oracledb.makedsn(host,1521,sid)

    sql = ' select * from sungjuk where sjno = :1 '
    conn = oracledb.connect(user=userid, password=passwd, dsn=dsn_tns)
    cursor = conn.cursor()


    cursor.execute(sql,[sjno])

    for sjno, name, kor, eng, mat, tot,avg,grd, regdate in cursor:
        print(sjno, name, kor, eng, mat, tot, avg, grd, regdate)

    cursor.close()
    conn.close()



# 성적 데이터 수정 시 수정할 데이터 입력받기
def read_again(sjno):
    """

    성적 데이터 수정 시 수정할 데이터 입력 받는 함수
    :param sjno:  수정할 학생 번호
    :return: 새롭게 생성된 성적데이터
    """
    sql = ' select name,kor,eng,mat from sungjuk where sjno = :1 '
    conn = oracledb.connect(user=userid, password=passwd, dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute(sql,[sjno])

    sj = [None,None,None,None]
    for  name, kor, eng, mat in cursor:
        sj = [name, kor, eng, mat]

    cursor.close()
    conn.close()


    if sj[0]: # 만일, 수정할 데이터가 존재한다면
        sj[0] = input(f'새로운 이름은? ({sj[0]}) : ')
        sj[1] = int(input(f'새로운 국어는? ({sj[1]}) : '))
        sj[2] = int(input(f'새로운 영어는? ({sj[2]}) : '))
        sj[3] = int(input(f'새로운 수학는? ({sj[3]})  : '))
        sj = compute_sungjuk(sj)

    return sj


# 성적 데이터 수정/삭제 시 변경사항 파일에 반영
def flush_sungjuk():
    """
    성적 데이터를 반영하는 함수
    :param: 없음
    :return: 없음
    """


# 성적 데이터 수정
def modify_sungjuk():
    """
    성적 데이터를 수정하는 함수
    :param: 없음
    :return: 없음
    """
    sjno = input('수정할 학생 번호는?')

    # 수정할 성적 데이터를 입력받고 성적처리한 결과를 받아옴
    sj = read_again(sjno)
    if sj[0]:
        sql = (' update sungjuk set name = :1 , kor = :2, eng = :3, mat = :4 ,'
               ' tot = :5, avg = :6, grd = :7, regdate = sysdate where sjno = :8')
        sj.append(sjno)

        conn = oracledb.connect(user=userid, password=passwd, dsn=dsn_tns)
        cursor = conn.cursor()

        cursor.execute(sql,sj)
        conn.commit()

        print(f'{cursor.rowcount} 건의 데이터가 수정되었습니다.')

        cursor.close()
        conn.close()

    else:
        print('찾는 데이터가 없습니다!')


# 성적 데이터 삭제
def remove_sungjuk():
    """
    성적 데이터를 삭제하는 함수
    :param: 없음
    :return: 없음
    """
    sjno = input('삭제할 학생 번호는?')
    sql = ' delete from sungjuk where sjno = :1 '
    conn = oracledb.connect(user=userid, password=passwd, dsn=dsn_tns)
    cursor = conn.cursor()

    cursor.execute(sql,[sjno])
    conn.commit()

    print(f'{cursor.rowcount}의 데이터가 삭제되었습니다')

    cursor.close()
    conn.close()

# 성적 처리 프로그램 종료
def exit_program():
    """

    성적처리 프로그램 종료 함수
    :param: 없음
    :return: 없음
    """
    print('프로그램 종료!')
    sys.exit(0)
