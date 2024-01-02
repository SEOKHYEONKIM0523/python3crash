def show_menu(): # 메뉴 출력
    main_menu = '''
    성적처리 프로그램 V5b
    -----------------
    1. 성적 데이터 추가
    2. 성적 데이터 조회
    3. 성적 데이터 상세 조회
    4. 성적 데이터 수정
    5. 성적 데이터 삭제
    0. 프로그램 종료
    -----------------
    '''
    print(main_menu)


def read_sungjuk(): #성적데이터 입력
    sj = {}
    sj['name'] = input('이름은?')
    sj['kor'] = int(input('국어 점수는?'))
    sj['eng'] = int(input('영어 점수는?'))
    sj['mat'] = int(input('수학 점수는?'))
    return sj

def compute_sungjuk(sj): # 성적 처리
    sj['tot'] = sj['kor'] + sj['eng'] + sj['mat']
    sj['avg'] = sj['tot'] / 3

    sj['grd'] = '수' if sj['avg'] >= 90 else \
        '우' if sj['avg'] >= 80 else \
        '미' if sj['avg'] >= 70 else \
        '양' if sj['avg'] >= 60 else '가'

def show_sungjuk(sungjuks): # 성적 데이터 출력
    for sjs in sungjuks['response']['body']['items']:
        print(f"이름 : {sjs['name']:s}, 국어: {sjs['kor']}, 영어: {sjs['eng']}, 수학: {sjs['mat']}")