import functools


def show_menu(): # 메뉴 출력
    main_menu = '''
    성적처리 프로그램 V6
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

def show_sungjuk(): # 성적 데이터 출력
    print('성적 데이터 조회')
    with open('sungjuks.csv', encoding='utf8') as f:
        sjs = f.readlines()
    for sj in sjs:
        item = sj.split(',')
        print(f"이름 : {item[0]:s}, 국어: {item[1]}, "
              f"영어: {item[2]}, 수학: {item[3]}")


def save_sungjuk(sj):
    with open('sungjuks.csv', 'a',encoding='utf8') as f:
        row = (f"{sj['name']},{sj['kor']},{sj['eng']},{sj['mat']},"
               f"{sj['tot']},{sj['avg']:.1f},{sj['grd']}\n")
        f.write(row)


def addsungJuk():
    print('성적 데이터 추가')
    sj = read_sungjuk()
    compute_sungjuk(sj)
    save_sungjuk(sj)  # 성적 데이터를 파일에 저장