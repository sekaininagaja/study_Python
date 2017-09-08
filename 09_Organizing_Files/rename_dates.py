#! python3
# renae_dates.py - Rebanes filenames wuth American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import shutil, os, re

# Create a regex that maches files with the Amerigan date format.
date_pattern = re.compile(r"""^(.*?) # 「日付」前のすべてのテキスト
    ((0|1)?\d)-     # "01～09月" or "10～12月"
    ((0|1|2|3)?\d)- # "01～09日" or "10～19日" or "20～29日" or "30～31日"
    ((19|20)\d\d)   # "19XX年" or "20XX年"
    (.*?)$          # 「日付」後のすべてのテキスト
    """, re.VERBOSE)

# Loop over the files in the working directory.
for amer_filename in os.listdir('.'):
    mo = date_pattern.search(amer_filename)

    # Skip files without a date.
    if mo == None:
        continue

    # Get the different parts of the filename.
    before_part = mo.group(1)
    month_part  = mo.group(2)
    day_part    = mo.group(3)
    year_part   = mo.group(6)
    after_part  = mo.group(8)

# Form the European-style filename.
euro_filename = "before_part + day_part + '-' + month_part + '-' + year_part + after_part"

# Get the full, absolute file paths.
abs_working_dir = os.path.abspath('.')
amer_filename = os.path.join(abs_working_dir, amer_filename)
euro_filename = os.path.join(abs_working_dir, euro_filename)
# shutil.move(amer_filename, euro_filename)     # テストが終わったらコメントをはずす

# Rename the files.
print('Renaming "%s" to "%s" ...' % (amer_filename, euro_filename))
