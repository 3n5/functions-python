"""配列の転置""""
import datetime
import csv

#------------------------------------------------------------------------------------------------------------
folder_name=""
file_namae="test"
#------------------------------------------------------------------------------------------------------------
"""
['1', '2', '3']
['4', '5', '6']
['7', '8', '9']
"""
def csv_yomikomi():
    read_fp=csv.reader(open("test.csv", "r"))
    _matrix=[]
    for line in read_fp:
        _matrix.append(line)
    #print(_matrix)
    return _matrix


def transpose(list):
    a = []
    b = []
    for ii in range(len(list[0])):
        for i in range(len(list)):
            a.append(list[i][ii])
        b.append(a)
        a = []
    return(b)
    
if __name__ == '__main__':
    #print(csv_yomikomi())
    #[['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    #print(transpose(csv_yomikomi()))
    #[['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9']]
