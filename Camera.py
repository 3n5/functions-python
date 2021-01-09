"""カメラ撮影"""
import cv2
import datetime
import time
fileName = "PIC_" + datetime.datetime.today().strftime('%Y%m%d_%H%M%S') + ".png"

# 内蔵カメラのIDは0、USBで接続したカメラは1以降。
capture = cv2.VideoCapture(1)
time.sleep(2)

# 画像データは変数imageに格納。retは取得成功変数。
ret, image = capture.read()
if ret == True:
    cv2.imwrite(fileName, image)
    print("taking picture is completed!!")
    capture.release()