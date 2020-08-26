"""csvの読み込みと書き出し"""

"""
src.csv
1 2 3
4 5 6
7 8 9

dst.csv
3
6
9
"""
import csv
with open('src.csv', newline='') as fin,    \
        open('dst.csv', 'w', newline='') as fout:

    reader = csv.reader(fin)
    writer = csv.writer(fout)

    for line in reader:
        writer.writerow(line[2:]) #
        #writer.writerow(line[0:2]) # [以上:未満]