#! python3

#
# strip()
# 先頭または末尾に空白(または任意の文字)を含まない新しい文字列を返す
#
# 文字列以外の引数が渡されない場合、空白文字は文字列の先頭と末尾から削除されます。
# それ以外の場合は、関数の2番目の引数で指定された文字が文字列から削除されます。
#

import re

def strip_mitaina(text, rmchar):

    # 除去する文字のチェック
    if rmchar == '':
        regex1 = re.compile(r'^\s+')
        regex2 = re.compile(r'\s+$')
    else:
        # 正規表現中で変数を使いたい場合
        regex1 = re.compile(r'^%s+' % rmchar)
        regex2 = re.compile(r'%s+$' % rmchar)

    mo = regex2.sub('', regex1.sub('', text))
    print(mo)

print('Please input message.')
message = str(input())

print('Please input remove charcter.')
remove_caracter = str(input())

# デバッグ用
# import pdb; pdb.set_trace()
strip_mitaina(message, remove_caracter)
