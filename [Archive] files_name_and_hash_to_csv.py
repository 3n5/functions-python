"""Check the hash of the file and save it as csv"""
import csv
import glob
import hashlib
import pandas
import datetime
import os
import time

target_dir = r'C:/Users/user/Downloads/reference_survey'# Folder with the files you want to save
save_folder=r'C:/Users/user/Desktop'# csv file save destination

# Get a list of files / folders to get the name and hash value
files = glob.glob(target_dir + '/*')
data=[]
print(len(files)*0.2/60,' min')
for file in files:
    # Get only the file name (no extension)
    file_name=os.path.basename(file)
    # Open the file and look up the hash (sha256) value 
    with open(file, 'rb') as f:
        body = f.read()
    hash_num = hashlib.sha256(body).hexdigest()
    _data=[file_name,hash_num]
    data.append(_data)
    time.sleep(0.2)

# Save as CSV
data=pandas.DataFrame(data)
data.to_csv("{0}/{1:%Y%m%d%H%M}.csv".format(save_folder,datetime.datetime.now()),encoding='utf_8_sig')