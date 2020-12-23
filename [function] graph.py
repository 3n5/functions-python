import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

#DATA
_A=[1,2,3,4,5,6,7,8,9]
_B=[0,1,2,4,8,4,2,1,0]
_C=[1,2,3,4,5,4,3,2,1]
Data_1D=[_A,_B]#list
Data_2D=[_A,_B,_C]#list
Data_1D = np.array(Data_1D)#ndarray
Data_2D = np.array(Data_2D)#ndarray

##import CSV
#df = pd.read_csv("amp.csv",encoding='UTF-8', header=None, engine='python') # File名を入力
#data1 = df.values[1:,1:,] #カラムを除いたデータ読み込み

##2D matrix
_x=Data_2D[0,:]#[1 2 3 4 5 6 7 8 9]
cnt_x=int(len(_x))#9
_y=Data_2D[:,0]#[1 0 1]
cnt_y=int(len(_y))#3
_x_center=Data_2D[int(cnt_y//2),:]#x center value
_y_center=Data_2D[:,int(cnt_x//2)]#y center value 縦1ライン
print(_x_center)


##graph parameter
res_x,res_y=0.5,0.5
x_scale=np.arange(-1*(cnt_x//2)+0.5, (cnt_x//2)+0.5, 1)*res_x if cnt_x%2 == 0 else np.arange(-1*(cnt_x//2), (cnt_x//2)+1, 1)*res_x
y_scale=np.arange(-1*(cnt_y//2)+0.5, (cnt_y//2)+0.5, 1)*res_y if cnt_x%2 == 0 else np.arange(-1*(cnt_y//2), (cnt_y//2)+1, 1)*res_y

fig = plt.figure(1,figsize=(10,10))
ax= fig.add_subplot(1,1,1)
ax.spines['top'].set_linewidth(0)
ax.spines['bottom'].set_linewidth(0)
ax.spines['right'].set_linewidth(0)
ax.spines['left'].set_linewidth(0)
plt.tick_params(labelbottom=False,labelleft=False,labelright=False,labeltop=False,
                bottom=False,left=False,right=False,top=False)

#plt.xlim([xmin,xmax])
#plt.ylim([ymin,ymax])
#plt.title(title, fontsize=title_size)  # グラフタイトル
#plt.xlabel(xlabel, fontsize=xlabel_size)  # 横軸タイトル
#plt.ylabel(ylabel, fontsize=ylabel_size)  # 縦軸タイトル

#plt.plot(Data_1D[0,:], Data_1D[1,:],c="black") #1D折れ線
#plt.scatter(Data_1D[0,:], Data_1D[1,:], c="black") #1D散布図
#plt.plot(x_scale, _x_center,c="red") #2Dグラフののx1lineの折れ線

plt.pcolor(x_scale, y_scale, Data_2D,cmap="rainbow")#2Dグラフ

plt.show()
file_name="ok"
plt.savefig(file_name, format='png', dpi=800)

