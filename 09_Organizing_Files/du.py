#! python3
# 特定フォルダツリー以下で指定サイズ以上のファイルやフォルダを検索するプログラムを作成します。
# ファイルのサイズを取得するには、osモジュールのos.path.getsize()を使用する。
# これらのファイルを絶対パスで画面に表示する。

import os, shutil

target_dir = '/Users/path/to/dir/study_python'
size = 10000

for foldername, subfolders, filenames in os.walk(target_dir):

    for filename in filenames:

        filepath = foldername + '/' + filename
        filesize = os.path.getsize(filepath)

        if size < filesize:
            print(str(os.path.getsize(filepath)) + ': ' + filepath)
