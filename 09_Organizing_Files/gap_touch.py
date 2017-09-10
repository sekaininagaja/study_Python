#! python3
# spam001.txt、spam002.txtなどの特定の接頭辞を持つすべてのファイルを1つのフォルダに格納し、
# 番号の隙間を見つけ出すプログラムを作成します。
#（spam001.txt と spam003.txt があるけど spam002.txt はない場合など）
# 番号の付いたファイルにギャップを挿入して新しいファイルを追加できる別のプログラムを作成します。

import os, shutil, re

target_dir = '/tmp/test'
source_file = '/tmp/test/source.txt'

for foldername, subfolders, filenames in os.walk(target_dir):

    # 走査する範囲をきめる(最後の対象ファイルの数字部分を得る)
    for filename in filenames:
        target_file_regex = re.compile(r'(sample\d{3}\.txt)')
        mo = target_file_regex.search(filename)
        if mo != None:
            end = mo.group()
        else:
            pass

    # 対象ファイルのうち、一番大きいファイル名の数字部分をぬきだす
    end_range_regex = re.compile(r'\d{3}')
    mo = end_range_regex.search(end)
    end = int(mo.group())

    # 最後の対象ファイルの数字部分までwhileでまわす
    i = 0
    while i < end :

        # iの値によって new_filenameを決定する
        # i が3桁に満たない場合はゼロパディングする
        num = '%03d'%(i+1)

        # 存在しない場合は new_filename を作成する(source.txtをコピーする)
        print('===sample%s.txt===' % num)
        new_filename = os.path.join(target_dir, 'sample%s.txt' % num) # 新しいファイル名
        if os.path.exists(new_filename) == False :
            print('作成するファイル名: ' + new_filename)
            shutil.copy(source_file, new_filename)
        else:
            print('すでに存在しています')
        i += 1
