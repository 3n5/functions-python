#Time-related functions  2020/12/22

"""Get elapsed time"""#[関数] プログラムの計測時間の表示
def time_elapsed(): 
    import time
    print(__doc__)
    start = time.time()
    print('== Replace the program you want to time here ==') and time.sleep(1)
    end = time.time()
    _time=end-start
    hour,min,sec=_time//3600,_time//60,_time%60
    print(f'It takes about {hour:.0f} hours {min:.0f} min {sec:.0f} sec')
    return 0
time_elapsed()

"""Get the current time"""
def time_current():
    import datetime
    print(__doc__)
    current=datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
    print(current)
time_current()