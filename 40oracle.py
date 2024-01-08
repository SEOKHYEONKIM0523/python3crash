# Oracle DB 로 데이터 다루기 1 - select

# cx_Oracle 모듈을 먼저 설치해야 함 - pip install cx_Oracle

# 1)Oracle instant client 버전에 따라 VS 재배포 패키지 설치
# 2)Oracle instant client를 다운로드하고, c:/Java에 압축해제
# 3)Oracle instant client 설치 경로를 시스템의 PATH 환경변수에 등록 후
# 4)intelliJ를 다시 시작

# oracle 클라이언트 라이브러리 설치
# oracle.github.io/odpi/doc/installation.html#windows
# cx-oracle.readthedocs.io/en/latest/user_guide/installation.html

# 주의!
# 오라클 인스턴스 클라이언트 라이브러리 버젼과
# visual studio C++ 재배포 버젼이 일치해야 제대로 실행됨!

# For Instant Client 21 install VS 2019 or later.
# For Instant Client 19 install VS 2017.
# https://www.oracle.com/kr/database/technologies/instant-client/winx64-64-downloads.html
# cx-oracle.readthedocs.io/en/latest/user_guide/installation.html

# intelliJ에서 csv 파일 가져올 시
# 텍스트 컬럼은 자동으로 CLOB 타입으로 설정
# CLOB가 꼭 필요한 컬럼을 제외하고 varchar 타입으로 바꿀 것을 추천

# 2024-01-08 기준
# cx_Oracle 모듈이 oracledb로 업그레이드 됨
# pip install oracledb




import cx_Oracle

import oracledb

host =''
userid = ''
passwd = ''
sid = 'FREE'

# DB 서버에 연결
#dsn_tns = cx_Oracle.makedsn(host,1521,sid)
#conn = cx_Oracle.connect(userid, passwd, dsn_tns)
dsn_tns = oracledb.makedsn(host,1521,sid)
conn = oracledb.connect(user=userid, password=passwd, dsn=dsn_tns)

cursor = conn.cursor()

sql = 'select first_name , last_name from employees'
cursor.execute(sql)

for fname, lname in cursor:
    print(fname, lname)

cursor.close()
conn.close()

# 국가별 메달별 획득 수 조회

# DB 서버에 연결

# dsn_tns = cx_Oracle.makedsn(host,1521,sid)
# conn = cx_Oracle.connect(userid, passwd, dsn_tns)
dsn_tns = oracledb.makedsn(host,1521,sid)
conn = oracledb.connect(user=userid, password=passwd, dsn=dsn_tns)

cursor = conn.cursor()

sql = (" SELECT COUNTRY, MEDAL, COUNT(Medal) cnt"
       " FROM SUMMERMEDALS2 GROUP BY COUNTRY, MEDAL "
       " ORDER BY COUNT(MEDAL) DESC ")
cursor.execute(sql)

for COUNTRY, MEDAL, medal_count in cursor:
    print(COUNTRY, MEDAL, medal_count)

cursor.close()
conn.close()

# 승선위치별(embarked) 성별(sex) 생존자 수(survived) 조회
# dsn_tns = cx_Oracle.makedsn(host,1521,sid)
# conn = cx_Oracle.connect(userid, passwd, dsn_tns)

dsn_tns = oracledb.makedsn(host,1521,sid)
conn = oracledb.connect(user=userid, password=passwd, dsn=dsn_tns)

cursor = conn.cursor()

sql = ( " SELECT EMBARK_TOWN, SEX , COUNT(ALIVE) alives FROM TITANIC2 "
        " where ALIVE = 'yes' "
        " GROUP BY EMBARK_TOWN ,SEX ORDER BY EMBARK_TOWN, SEX")
cursor.execute(sql)

for EMBARKED, SEX , alives in cursor:
    print(EMBARKED, SEX, alives)

cursor.close()
conn.close()

# 승선위치별(embarked) 사람(who) 생존자 수(survived) 조회
# dsn_tns = cx_Oracle.makedsn(host,1521,sid)
# conn = cx_Oracle.connect(userid, passwd, dsn_tns)

dsn_tns = oracledb.makedsn(host,1521,sid)
conn = oracledb.connect(user=userid, password=passwd, dsn=dsn_tns)

cursor = conn.cursor()


sql = ( " SELECT EMBARK_TOWN, SEX , COUNT(ALIVE) alives FROM TITANIC2 "
        " where ALIVE = 'yes' "
        " GROUP BY EMBARK_TOWN ,SEX ORDER BY EMBARK_TOWN, SEX")

cursor.execute(sql)

for EMBARKED, who , alives in cursor:
    print(EMBARKED, who, alives)

cursor.close()
conn.close()
