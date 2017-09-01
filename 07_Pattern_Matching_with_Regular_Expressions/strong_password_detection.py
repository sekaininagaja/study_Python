#! python3
# 強力なパスワード検出プログラム

import re

def ok_message():
    print('OK: This passsword is strong.')

def ng_message(flag):
    if flag == 'length':
        print('NG: This password is too short. (must be over 8 char)')
    elif flag == 'number':
        print('NG: This password has not number. (must be contain at least 1 number)')
    elif flag == 'uppercase':
        print('NG: This password has not uppercase. (must be contain uppercase)')
    elif flag == 'lowercase':
        print('NG: This password has not lowercase. (must be contain lowercase)')
    else:
        print('NG: Weak password!')

def check_text(text):

    check_length_regex = re.compile(r'.{8,}')
    check_number_regex = re.compile(r'[0-9]')
    check_lowercase_regex = re.compile(r'[a-z]')
    check_uppercase_regex = re.compile(r'[A-Z]')

    if check_length_regex.search(text) != None:
        if check_number_regex.search(text) != None:
            if check_uppercase_regex.search(text) != None:
                if check_lowercase_regex.search(text) != None:
                    ok_message()
                else:
                    ng_message('lowercase')
            else:
                ng_message('uppercase')
        else:
            ng_message('number')
    else:
        ng_message('length')

# パスワードを入力
print('Input Password: ')
r_password = str(input())   # 生パスワード

check_text(r_password)
