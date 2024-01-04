import sys
import json
from collections import OrderedDict

# sungjuks = {'response' :{'body':{'totalCount':999, 'items': []}}}
sjs = {'response' :{'body':{'totalCount': 0, 'items': []}}}
items = []
totalCount = 0


def show_menu(): # 메뉴 출력
    main_menu = '''
    성적처리 프로그램 V6c
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
    sungjuk = input('이름과 성적을 입력하세요 (예 : 홍길동 99 98 99)')
    data = sungjuk.split()
    sj = OrderedDict()
    sj['name'] = data[0]
    sj['kor'] = int(data[1])
    sj['eng'] = int(data[2])
    sj['mat'] = int(data[3])
    return sj

def compute_sungjuk(sj): # 성적 처리
    sj['tot'] = sj['kor'] + sj['eng'] + sj['mat']
    sj['avg'] = float(f"{sj['tot'] / 3:.1f}")


    sj['grd'] = '수' if sj['avg'] >= 90 else \
        '우' if sj['avg'] >= 80 else \
        '미' if sj['avg'] >= 70 else \
        '양' if sj['avg'] >= 60 else '가'

def show_sungjuk(): # 성적 데이터 출력
    print('성적 데이터 조회')
    for sj in sjs['response']['body']['items']:
        print(f"이름 : {sj['name']:s}, 국어: {sj['kor']}, "
              f"영어: {sj['eng']}, 수학: {sj['mat']}")


def save_sungjuk(sj):
    # 메모리 내에 생성된 json 객체에 방금 생성한 성적데이터 저장
    items.append(sj)
    sjs['response']['body']['totalCount'] += 1
    # 메모리 내에 생성된 json 객체를 파일에 저장
    with open('sungjuks.json', 'w',encoding='utf8') as f:
        json.dump(sjs, f, ensure_ascii=False)


def addsungJuk():
    print('성적 데이터 추가')
    sj = read_sungjuk()
    compute_sungjuk(sj)
    save_sungjuk(sj)  # 성적 데이터를 파일에 저장


# 프로그램 시작 시 sungjuks.jason 파일을 읽어 sjs 변수에 초기화
def load_sungjuk():
    global sjs,items,totalCount

    try:           # 작업 중에 오류가 발생하면
        with open('sungjuks.json',encoding='utf8') as f:
            sjs = json.load(f)
            items = sjs['response']['body']['items']
            totalCount = sjs['response']['body']['totalCount']
    except:
        items = sjs['response']['body']['items']
        totalCount = sjs['response']['body']['totalCount']



def showone_sungjuk():
    name = input('상세 조회할 학생 이름은? ')
    info = '찾는 데이터가 없습니다'

    for sj in sjs['response']['body']['items']:
        if sj['name'] == name:
            info = (f"{sj['name']} {sj['kor']} {sj['eng']} {sj['mat']}"
                    f"{sj['tot']} {sj['avg']} {sj['grd']}")
            break

    print(info)

def read_again(data, name):
    kor = int(input(f'새로운 국어는? ({data["kor"]}) : '))
    eng = int(input(f'새로운 영어는? ({data["eng"]}) : '))
    mat = int(input(f'새로운 수학는? ({data["mat"]})  : '))

    data = OrderedDict()
    data['name'] = name
    data['kor'] = kor
    data['eng'] = eng
    data['mat'] = mat
    return data


def flush_sungjuk():
    with open('sungjuks.json', 'w',encoding='utf8') as f:
        json.dump(sjs, f, ensure_ascii=False)


def modify_sungjuk():
    name = input('수정할 학생 이름은?')

    # 수정할 학생 데이터를 이름으로 찾음
    data = None
    idx = None
    for i, sj in enumerate(items):
        if sj['name'] == name:
            data = sj
            idx = i

    # 수정할 학생 데이터를 찾았다면
    # 새로운 값을 입력받고, 다시 성적처리함
    if data:
        data = read_again(data,name)
        compute_sungjuk(data)

        #리스트에 기존 데이터를 버리고 새로운 데이터로 재설정
        items[idx] = data

        #변경 사항을 json 파일에 반영
        flush_sungjuk()

    else:
        print('찾는 데이터가 없습니다!')

def remove_sungjuk():
    name = input('삭제할 학생 이름은?')

    # 삭제할 데이터를 찾음
    data = None
    for sj in items:
        if sj['name'] == name:
            data = sj
            break
    # 삭제할 데이터를 찾았다면
    if data:
        confirm = input('정말로 삭제하시겠습니까? (yes/no)')
        if confirm == 'yes':
            items.remove(data)
            sjs['response']['body']['totalCount'] -= 1
            print(f'{name}의 데이터가 삭제되었습니다')
            flush_sungjuk()
        else:
            print('삭제가 취소되었습니다')

def exit_program():
    print('프로그램 종료!')
    exit(0)
