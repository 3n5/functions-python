"""Check the hash of the file and output (or delete) if it is duplicated"""
"""ファイルのハッシュを確認して重複した場合に出力(or削除)"""
#ref https://news.mynavi.jp/article/zeropython-25/
import os, glob, hashlib

# 重複ファイルがあるかどうかを調べるディレクトリ
target_dir = './check'
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
    #print(v)
    if v in body_dict: # 重複しているか --- (*4)
        f2 = body_dict[v]
        # 念のため実際に合致しているか調べる --- (*5)
        if body == get_body(f2):
            print(f, "==", f2)
            # 実際に削除するなら以下のコメントを外す ---- (*5a)
            # os.remove(f)
    else:
        body_dict[v] = f # --- (*6)
print("fin")