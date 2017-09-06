#! python3

import re, os, sys

template_file = open('hoge.txt')
template_file_content = template_file.read()

placeholder_regex = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
mo = placeholder_regex.findall(template_file_content)
replacement_word = []

for i in range(len(mo)):
    if mo[i] == 'ADJECTIVE':
        replacement_word = replacement_word + [input('Please input ADJECTIVE: ')]
    elif mo[i] == 'NOUN':
        replacement_word = replacement_word + [input('Please input NOUN: ')]
    elif mo[i] == 'VERB':
        replacement_word = replacement_word + [input('Please input VERB: ')]
    elif mo[i] == 'ADVERB':
        replacement_word = replacement_word + [input('Please input ADVERB: ')]
    i += 1

print(replacement_word)
template_file.close()
