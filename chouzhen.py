# -*- coding:utf8 -*-
import cv2
import os
import shutil
 
 
def get_frame_from_video(video_name, interval):
    """
    Args:
        video_name:输入视频名字
        interval: 保存图片的帧率间隔
    Returns:
    """
 
    # 保存图片的路径
    save_path = video_name.split('.mp4')[0] + '/images/'
    is_exists = os.path.exists(save_path)
    if not is_exists:
        os.makedirs(save_path)
        print('path of %s is build' % save_path)
    else:
        shutil.rmtree(save_path)
        os.makedirs(save_path)
        print('path of %s already exist and rebuild' % save_path)
 
    # 开始读视频
    video_capture = cv2.VideoCapture(video_name)
    i = 0
    j = 0
 
    while True:
        success, frame1 = video_capture.read()
        frame = cv2.resize(frame1, (1280,720), interpolation=cv2.INTER_AREA)
        i += 1
        if i % interval == 0:
            # 保存图片
            j += 1
            save_name = save_path + str(j) + '.jpg'
            cv2.imwrite(save_name, frame)
            print('image of %s is saved' % save_name)
        if not success:
            print('video is all read')
            break
 
 
if __name__ == '__main__':
    # 视频文件名字
    video_name = './vedio/data14.mp4'
    interval = 10
    get_frame_from_video(video_name, interval)