#! python3
# spam001.txt、spam002.txtなどの特定の接頭辞を持つすべてのファイルを1つのフォルダに格納し、
# 番号の隙間を見つけ出すプログラムを作成します。
#（spam001.txt と spam003.txt があるけど spam002.txt はない場合など）
# このギャップを閉じるために、後のすべてのファイルの名前をプログラムに変更させます。

import os, shutil, re

target_dir = '/tmp/test'
target_file_list = []

for foldername, subfolders, filenames in os.walk(target_dir):

    # 対象ファイルのリストをつくる
    for filename in filenames:
        target_file_regex = re.compile(r'sample\d{3}\.txt')
        mo = target_file_regex.search(filename)
        if mo != None:
            target_file_list = target_file_list + [mo.group()]
        else:
            pass

    # 対象リストのファイル数だけforでまわす。
    for i in range(len(target_file_list)):
        new_filename     = os.path.join(target_dir, 'sample00%s.txt' % (i+1)) # 新しいファイル名
        current_filename = os.path.join(target_dir, target_file_list[i])      # リネーム対象ファイル名

        # 新しいファイル名とリネーム対象ファイル名が異なる場合は、リネームする。
        # 新しいファイル名とリネーム対象ファイル名が同じ場合は、ファイルが既に存在するのでなにもしない
        print('===sample00%s.txt===' % (i+1))
        if current_filename != new_filename:
            print('リネームする対象: ' + current_filename)
            print('リネーム後の名称: ' + new_filename)
            shutil.move(current_filename, new_filename)
        else:
            print('すでに存在しています')
        i += 1
