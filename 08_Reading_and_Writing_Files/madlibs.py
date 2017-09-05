#! python3

import re, os

template_file = open('hoge.txt', 'r')
template_file_content = template_file.read()

print(template_file_content)

template_file.close()
