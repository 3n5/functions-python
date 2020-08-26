"""
sample.txtの中のファイルをfolderへ移動する
"""

import os
import glob
import shutil

folder="to"
target = '{}'.format(folder) + os.sep  # os.sep == /
for line in open('sample.txt', 'r'):
    line = line.strip() 
    print(line)   
    files = glob.glob(line)
    if len(files) == 1:
        print(files[0])
        shutil.move(files[0], target)


