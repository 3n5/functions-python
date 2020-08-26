"""プログラムの計測時間の計測"""
import time
import datetime

start = time.time()
start_time = datetime.datetime.now()

############################
#ここに計測したいプログラムを入れる
time.sleep(2)
############################
end = time.time()
finish_time = datetime.datetime.now()

time=end-start
hour=int(time/3600)
min=int(time/60)
sec=int(time%60)
print("{0} 時間 {1} 分 {2} 秒かかりました。".format(hour,min,sec))
print("開始時間:",start_time)
print("終了時間:",finish_time)