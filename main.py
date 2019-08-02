import keyboard
import signal
import sys
import time
import re
import os
import getpass
from colorama import Fore, Style, Back, init

def signal_handler(sig, frame):
    print('\n\nBye!')
    # print('You pressed Ctrl+C!')
    sys.exit(0)

def main():
    line = ''
    pressed = False
    curUser = getpass.getuser()
    while True:
        lineLst = line.split()

        if lineLst == []:
            cmd = ''
        else:
            cmd = lineLst[0]

        if cmd == 'print':
            print(lineLst[1])
        print("{}({}@bd-shell){} ".format(Fore.GREEN, curUser, Style.RESET_ALL), end='')
        line = input()

if __name__ == '__main__':
    init()
    signal.signal(signal.SIGINT, signal_handler)

    main()

    