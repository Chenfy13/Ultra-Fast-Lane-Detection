import cv2
import os

def get_file_names(search_path):
    for (dirpath, _, filenames) in os.walk(search_path):
        for filename in filenames:
            yield filename  # os.path.join(dirpath, filename)

def save_to_video(output_path, output_video_file, frame_rate):
    list_files = sorted([int(i.split('_')[-1].split('.')[0]) for i in get_file_names(output_path)])
    # 拿一张图片确认宽高
    img0 = cv2.imread(os.path.join(output_path, '%s.jpg' % list_files[0]))
    # print(img0)
    height, width, layers = img0.shape
    # 视频保存初始化 VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    videowriter = cv2.VideoWriter(output_video_file, fourcc, frame_rate, (width, height))
    # 核心，保存的东西
    for f in list_files:
        f = '%s.jpg' % f
        # print("saving..." + f)
        img = cv2.imread(os.path.join(output_path, f))
        videowriter.write(img)
    videowriter.release()
    cv2.destroyAllWindows()
    print('Success save %s!' % output_video_file)
    pass

# 图片变视频
output_dir = './'
output_path = '/home/chen/fsdownload/data14_culane'  # 输入图片存放位置
output_video_file = './data14_culane.mp4'  # 输入视频保存位置以及视频名称
save_to_video(output_path, output_video_file, 10)
