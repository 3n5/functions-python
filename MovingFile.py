"""Move the files that match the csv list to another folder."""

def file_move_based_on_csv():
    import shutil
    import glob
    import csv
    _from=r'C:/Users/USER/Desktop/_from' #Source directory #[[apple],[banana],[grape]]
    _to=r'C:/Users/USER/Desktop/_to'   #Destination Directory []
    _csv=r'C:/Users/USER/Downloads/archive/reference.csv'#[[apple],[banana]]
    with open(_csv, 'r') as csvfile:  # , encoding='shift_jis'
        csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for file1 in csv_reader:
            file = glob.glob('{0}/[{1}*'.format(','.join(file1)))
            if len(file) == 0:
                pass
            elif len(file) == 1:
                shutil.move(','.join(file), _to)
                #shutil.copy(','.join(file),_to )
            else:
                for file2 in file:
                    shutil.move(file2, _to)
                    #shutil.copy(i2,_to) #if copy
