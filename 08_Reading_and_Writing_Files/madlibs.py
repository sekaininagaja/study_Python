#! python3

import re
import os
import sys

template_file = open('hoge.txt')
template_file_content = template_file.read()

placeholder_regex = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
print(placeholder_regex.findall(template_file_content))
mo = placeholder_regex.search(template_file_content)

template_file.close()
