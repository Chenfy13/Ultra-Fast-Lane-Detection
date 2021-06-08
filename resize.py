import os
import sys
import cv2

img_path = 'data1/images'
#gt_path = 'didi3/images2'


def read_path(file_pathname):
    #遍历该目录下的所有图片文件
    for filename in os.listdir(file_pathname):
        #print(filename)
        img = cv2.imread(file_pathname+'/'+filename)
        new_image = cv2.resize(img, (1640,590), interpolation=cv2.INTER_AREA)
        #####保存图片的路径
        cv2.imwrite(img_path+"/"+filename, new_image)


read_path(img_path)
#print(os.getcwd())