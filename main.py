import keyboard
import signal
import sys
import time
import re
import os
import getpass
import clipboard
from colorama import Fore, Style, Back, init

state = [] # 현재 쉘에서 어느 위치에 있는지 나타내는 변수

dir_tree = {
        'name':'root',
        0: {
            'name':'모델(models)'
            },
        1: {
            'name':'측정방법(metrics)',
            0: {
                'name': 'RMSE',
                'content': 'metrics/rmse.py'
                }
            }
        }

def signal_handler(sig, frame):
    print('\n\nBye!')
    # print('You pressed Ctrl+C!')
    sys.exit(0)


def interpreter(cmd): # dummy function
    pass

def __print(*args): # dummy function
    for i in args:
        print(i, end=' ')
    print('')

def __list(): #TODO: list 대신 링크드 리스트로 노드를 연결할 방법이 더 나은지?\
    global state
    global dir_tree

    d = dir_tree #TODO: 계속 찾아들어가게 하지 말고 현재 위치를 저장하는 글로벌 변수를 만들 것
    if state:
        for i in state:
            d = d[i]


    for key in d:
        if key == 'name':
            print("========================")
            print('현재 위치: %s' % d[key])
            print("========================")
        elif key == 'content':
            pass
        else:
            print(key, d[key]['name'])

def __select(*args): #TODO: select를 할 수 없는 상태인지 체크하기.
    global state
    a = int(args[0])
    state.append(a)

def __back(): #TODO: back을 할 수 없는 상태인지 체크하기.
    global state
    state.pop()


def __show():
    global state
    global dir_tree

    d = dir_tree #TODO: 계속 찾아들어가게 하지 말고 현재 위치를 저장하는 글로벌 변수를 만들 것
    if state:
        for i in state:
            d = d[i]

    with open(d['content'], 'rt', encoding='utf-8') as f:
        print(f.read())

def __copy():
    global state
    global dir_tree

    d = dir_tree #TODO: 계속 찾아들어가게 하지 말고 현재 위치를 저장하는 글로벌 변수를 만들 것
    if state:
        for i in state:
            d = d[i]

    with open(d['content'], 'rt', encoding='utf-8') as f:
        clipboard.copy(f.read())
    print("복사 되었습니다.")

def main():
    line = ''
    os.system("cls")
    pressed = False
    curUser = getpass.getuser()
    while True:
        lineLst = line.split()

        if lineLst == []:
            cmd = ''
        else:
            cmd = lineLst[0]

        if cmd == 'print':
            __print(*lineLst[1:])
        elif cmd == 'list':
            __list()
        elif cmd == 'select':
            __select(*lineLst[1:])
        elif cmd == 'back':
            __back()
        elif cmd == 'show':
            __show()
        elif cmd == 'copy':
            __copy()

        print("{}({}@bd-shell){} ".format(Fore.GREEN, curUser, Style.RESET_ALL), end='')
        line = input()

if __name__ == '__main__':
    init()
    signal.signal(signal.SIGINT, signal_handler)

    main()

    