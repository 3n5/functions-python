"""csvのリストに一致するファイルを別のフォルダに移動する。""""

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