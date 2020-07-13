import datetime
import shutil
import os

def file_into_folder():
    folder_name = 'folder'
    file1_name = 'test1.csv'

    now = datetime.datetime.now()
    folder_name = '{0:%H%M%S} {1}'.format(now, folder_name)  # %Y%m%d-
    os.mkdir(folder_name)
    shutil.move(file1_name, folder_name)

    #ss1 = file1_name.split(".", 1)
    #new_name1 = "{0}_{1:%Y%m%d-%H%M%S}.{2}".format(ss1[0], now, ss1[1])


