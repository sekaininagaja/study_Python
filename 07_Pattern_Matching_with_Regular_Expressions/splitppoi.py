#! python3

# split()
# 文字列値に対して呼び出すと、文字列のリストを返す。
# デリミタ指定なし(デフォルトのスペースで区切る)
# デリミタ指定あり(その文字列で区切る)

import re

def split_mitainamono(text,delimiter):

    # デリミタのチェック
    if delimiter == '':
        delimiter = ' ' # デリミタの指定がない場合はスペースを設定

    check_spase_regex = re.compile(r'\s')
    mo = check_spase_regex.sub(delimiter, text)
    print(mo)

print('Please input message.')
message = str(input())

print('Please input delimiter.')
delimiter = str(input())

split_mitainamono(message,delimiter)
