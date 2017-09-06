#! python3

import re, os

# 拡張子(.txt)
extention = re.compile(r'\.txt$')

# 検索する文字列(正規表現)
# 電話番号(090-xxxx-xxxx) をひっかけることにする
# 課題: 090-1234-2313241 にひっかかっちゃうのどうしよう・・・
search_regex = re.compile(r'^090-\d{4}-\d{4}')

# カレントディレクトリを対象ディレクトリとする
# カレントディレクトリ内のファイルをfiles変数に入れる
files = os.listdir('.')

# ファイル分ループする
for x in files:

    # 拡張子が .txt の場合、対象ファイルをopenする
    # 対象ファイルは readlines() で1行ずつ読み込む
    if extention.search(x):
        txtfile = open(x)
        txtfile_contents = txtfile.readlines()

        # ファイル名の表示用
        print('=== %s ===' % x)

        # 各ファイルの行数分ループする(txtfile_contentsの数)
        for i in range(len(txtfile_contents)):

            # 検索する文字列にマッチしたら、行数とともに表示する
            # 課題: readlines() で読み込むと1行ずつのリストになるが最後に改行がはいる。これどうやって消したらいいの・・・
            if search_regex.search(txtfile_contents[i]) != None :
                print('%s:  %s' % (i+1, txtfile_contents[i]))

        # ファイルをクローズ
        txtfile.close()
