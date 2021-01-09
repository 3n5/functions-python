####使わないやつはのせない
"""
配列の転置
フォルダの中のファイル名をCSV吐き出し
csvのリストに一致するファイルを別のフォルダに移動する
sample.txtの中のファイル名を持つファイルをfolderへ移動する。
複数回入力した値を記録してcsvで出力する。
csvの単語(縦列)をweb検索する。
"""


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






"""フォルダの中のファイル名をCSV吐き出し"""
import re
import os
import sys
import pandas as pd

files = os.listdir("C:/Users/USER/Desktop/M2")
namae_list=[]
for i in files:
    namae_list.append(i)
save_name = "./test.csv"
namae_list = pd.DataFrame(namae_list)
#namae_list=namae_list.T   横表示させたいとき
namae_list.to_csv('test.csv',  mode='w',index=False,  header=False,encoding="shift-jis")




"""csvのリストに一致するファイルを別のフォルダに移動する。----------------------------------""""

def file_move_based_on_csv():
    import shutil
    import glob
    import csv

    _from="C:/Users/USER/Desktop/_from" #source directory
    _to="C:/Users/USER/Desktop/_to"#Destination Directory
    _csv='C:/Users/USER/Downloads/archive/pdf5name.csv'#[[apple],[banana],[grape]]

    with open(_csv, 'r') as csvfile:  # , encoding='shift_jis'
        csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for i1 in csv_reader:
            file = glob.glob('{0}/[{1}*'.format(','.join(i1)))
            if len(file) == 0:
                pass
            elif len(file) == 1:
                shutil.move(','.join(file), _to)
                #shutil.copy(','.join(file),_to )
            else:
                for i2 in file:
                    shutil.move(i2, _to)
                    #shutil.copy(i2,_to) #if copy


"""sample.txtの中のファイル名を持つファイルをfolderへ移動する。--------------------"""
def file2folder_in_txt_lists():
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


"""csvの単語(縦列)をweb検索する。--------------------------------------"""
def search_words_in_csv():
    import webbrowser
    import csv

    with open('C:/Users/USER/Desktop/test.csv', 'r', encoding='shift_jis') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for file in csv_reader:
            webbrowser.open("{}".format(','.join(file)))
            #{}を"https://www.google.com/search?q={}"に変えれば単語検索
    print('fin')




'''複数回入力した値を記録してcsvで出力する。--------------------------------------'''
def list_output_csv(list,folder_name,file_name):
    import csv

    if folder_name=="":
        save_name="{}.csv".format(file_name)
    else:
        save_name = "{0}/{1}.csv".format(folder_name, file_name)
    csv_name = open(save_name, 'w', newline='')
    csvWriter = csv.writer(csv_name)
    csvWriter.writerows(list)
    csv_name.close()

output_val=[]
while(True):
    input_val=input("input words")
    output_val.append([input_val])
    if input_val=="":
        break

list_output_csv(output_val, "", "test")  # input_list, folder_name,file_name


a=r'test'
b=r'ans'

path_l=r'C:\Users\user\Desktop\list.txt'
#Ltxtへの書き込み
lists=[a,b]
with open(path_l, mode='w') as f:
    f.write('\n'.join(lists))

#読み込み
with open(path_l) as f:
    print(f.read())

import sys
if a=='test':
    sys.exit()
else:
    print("OJK")
