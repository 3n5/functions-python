"""ファイルのハッシュを確認してcsvで保存(名前が違った場合に使う)"""
import csv
import glob
import hashlib
import pandas
import datetime
import os

data=[]
save_folder="C:/Users/user/Desktop/_program"#確認先
target_dir = './新しいフォルダー'#保存先
body_dict = {}

# ファイルの内容を返す関数 --- (*1)
def get_body(fname):
    with open(fname, "rb") as f:
        return f.read()

# ファイルの一覧を得て重複があるか調べる --- (*2)
files = glob.glob(target_dir + "/*")
for f in files:
    # ファイルを開いてハッシュ値を調べる --- (*3)
    body = get_body(f)
    v = hashlib.sha256(body).hexdigest()
    data.append(v)
    
data=pandas.DataFrame(data)
data.to_csv(
    "{0} {1:%Y%m%d%H%M}.csv".format(save_folder,datetime.datetime.now()))
