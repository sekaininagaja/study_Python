#! python3
# フォルダツリーを走査して特定のファイル拡張子（.pdfや.jpgなど）を持つファイルを検索するプログラムを作成します。
# これらのファイルを、それらが入っている場所から新しいフォルダにコピーします。

import os, shutil, re

source_dir = '/Users/path/to/dir/study_python'
target_dir = '/Users/path/to/dir/study_python/backup'
extension = '.md'

# 特定ファイルを見つける
for folder_name, subfolders, filenames in os.walk(source_dir):

    for filename in filenames:

        # endswith で拡張子があつかえる
        # 拡張子チェック、target_dir以下は除外
        if filename.endswith(extension) and folder_name != target_dir:
            target_file = folder_name + '/' + filename
#            print(target_file)
            shutil.copy(target_file, target_dir)

# コピーする
