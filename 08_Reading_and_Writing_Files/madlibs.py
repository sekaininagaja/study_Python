#! python3

import re, os, sys

# テンプレートファイル(hoge.txt)をひらく。
# 結果出力用のファイル(kekka.txt) をひらく。※書き込みモード
template_file = open('hoge.txt')
resulut_file = open('kekka.txt', 'w')

# テンプレートファイルの内容を読み込む
template_file_content = template_file.read()

# 置き換える文字列の正規表現を作成。全体の置き換え文字列を得る。
placeholder_regex = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
mo = placeholder_regex.findall(template_file_content)

# 置き換え単語の入力。replacement_word変数にリストとして登録する。
# テンプレートファイル内に出現した置き換え元文字列は、はその都度入力した文字列に置き換える。
replacement_word = []
for i in range(len(mo)):
    if mo[i] == 'ADJECTIVE':
        replacement_word = replacement_word + [input('Please input ADJECTIVE: ')]
        template_file_content = template_file_content.replace('ADJECTIVE', replacement_word[i], 1)
    elif mo[i] == 'NOUN':
        replacement_word = replacement_word + [input('Please input NOUN: ')]
        template_file_content = template_file_content.replace('NOUN', replacement_word[i], 1)
    elif mo[i] == 'VERB':
        replacement_word = replacement_word + [input('Please input VERB: ')]
        template_file_content = template_file_content.replace('VERB', replacement_word[i], 1)
    elif mo[i] == 'ADVERB':
        replacement_word = replacement_word + [input('Please input ADVERB: ')]
        template_file_content = template_file_content.replace('ADBERB', replacement_word[i], 1)
    i += 1

# replacement_word変数の内容(入力した文字列で置き換え済み)をファイルに書き出す
resulut_file.write(template_file_content)

# 終了処理
template_file.close()
resulut_file.close()
