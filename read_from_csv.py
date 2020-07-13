import numpy as np
import csv

def csv_read_row():
    """
    input
    [1,2,3]
    output
    [1,2,3]
    """
    csv_file = open("test_row.csv", "r")
    f = csv.reader(csv_file)
    header = next(f)
    return header

def csv_read_col():
    """
    input
    [[1],
     [2],
     [3],]
    output
    [1,2,3]
    """
    csv_file = open("test_col.csv", 'r')
    _list = []
    for row in csv.reader(csv_file):
        _list.append(row[0])#line 0
    return _list


if __name__ == '__main__':
    csv_read_row()
    csv_read_col()




