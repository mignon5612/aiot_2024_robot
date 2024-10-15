import cv2
import numpy as np

def on_mouse(event, x, y, flags, param):
    src = param['src']
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        cv2.circle(param, (x,y), 10, (255,0,0), -1)
        cv2.imshow("img", param)

def main():
    folder = "/home/test/aiot_2024_robot/OpenCV/cppTest/data/"
    src = cv2.imread(folder + "lena.bmp", cv2.IMREAD_COLOR)

    param = src
    cv2.setMouseCallback("img", on_mouse, param)
    cv2.namedWindow("img")

    cv2.imshow("img", src)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
