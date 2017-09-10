#! python3
# spam001.txt、spam002.txtなどの特定の接頭辞を持つすべてのファイルを1つのフォルダに格納し、
# 番号の隙間を見つけ出すプログラムを作成します。
#（spam001.txt と spam003.txt があるけど spam002.txt はない場合など）
# このギャップを閉じるために、後のすべてのファイルの名前をプログラムに変更させます。

import os, shutil, re

target_dir = '/Users/eri/Qsync/study/study_python/09_Organizing_Files/test'

#def check_file_exist():
#    regex1 = re.compile(r'sample00[1-9].txt')  # 001 ~ 009
#    regex2 = re.compile(r'sample0[1-9][0-9].txt') # 010 ~ 099
#    regex3 = re.compile(r'sample[1-9][0-9][0-9].txt') # 100 ~ 999

start = ''
end = ''
rename_filename = ''

# 精査する範囲を決める関数
def input_range():
    global start, end

    while True:
        start = input('開始値を整数で入力してください(デフォルト1): ')
        if start.isdecimal():
            start = int(start)
            print('start: ' + str(start))
            break
        elif start == '':
            start = 1
            print('start: ' + str(start))
            break

    while True:
        end = input('終了値を整数で入力してください(デフォルト10): ' )
        if end.isdecimal():
            end = int(end)
        elif end == '':
            end = 10

        if start < end:
            print('end: ' + str(end))
            break
        else:
            print('終了(end)は開始(start)よりも大きい数字にしてください。')

# ファイルの存在をチェックする関数
def check_file_exist():
    global rename_filename

    # ファイルが存在しない場合
    if os.path.exists(check_filename) == False:
        print(check_filename + ': naiyo')
        if rename_filename == '':
            rename_filename = check_filename
        start = 1

    # ファイルが存在する(001)場合
    elif check_filename == os.path.join(target_dir, 'sample001.txt'):
        pass

    # ファイルが存在する(002〜999)場合
    else:
        print(check_filename + ': aruyo')
        print('リネーム対象: ' + check_filename)
        if rename_filename == '':
            rename_filename = os.path.join(target_dir, 'sample%s.txt' % start)
            print('リネーム名: ' + rename_filename)
        else:
            print('リネーム名: ' + rename_filename)
        start = 1

input_range()

# 精査する範囲内で番号の隙間を見つける
while(start <= end):

    if start < 10 :
        check_filename = os.path.join(target_dir, 'sample00%s.txt' % start)
        check_file_exist()

    elif (start >= 10) and (start < 100):
        check_filename = os.path.join(target_dir, 'sample0%s.txt' % start)
        check_file_exist()

    elif (start >= 100) and (start < 1000):
        check_filename = os.path.join(target_dir, 'sample%s.txt' % start)
        check_file_exist()

    start += 1




#for foldername, subfolders, filenames in os.walk(target_dir):

    # 対象ファイル名: sample000.txt 〜 sample999.txt
    # まず対象ディレクトリ内から対象ファイル名にマッチするものリストの中で一番大きい数字を探す

#    for filename in filenames:


#        regex = re.compile(r'sample\d{3}\.txt')
#        filenumber = ''
#        mo = regex.search(filename)

#        if mo != None:
#            filenumber_regex = re.compile(r'\d{3}')
#            filenumber = filenumber + filenumber_regex.search(filename)
#            print(filenumber)
#            matches.append(filenumber)
#            print(os.path.join(target_dir, filename))

#    while True:
#        if i < 10 :
#            check_filename = os.path.join(target_dir, 'sample00%s' % i)
#            if os.path.exists(check_filename) == False:
#                print(check_filename + ': naiyo')
#            elif
#                print(check_filename + ': aruyo')

#    print(matches)

#for foldername, subfolders, filenames in os.walk(target_dir):

#    i = 1
#    for filename in filenames:
#        if i < 10 :
#            check_filename = os.path.join(foldername, 'sample00%s' % i)
#            if os.path.exists(check_filename) == False:
#                print('naiyo')

#        print(check_filename)
#        print(i)
#        i += 1


#        print(str(check_num) + ': ' + filename)
#        i += 1
