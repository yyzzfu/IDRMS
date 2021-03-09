import os
import datetime
import random


# 获取文件夹中的文件
def get_file_from_directory(dirpath):
    for root, dirs, files in os.walk(dirpath):
        for file in files:
            return os.path.join(root, file)


# 将文件夹中的文件名改名，并返回修改后的文件名
def modify_filename_and_return_filename(dirpath, file_type='.jpg'):
    filename = str(datetime.datetime.now())
    filename_1 = filename.replace(':', "_")
    filename_2 = filename_1.replace('.', "_")
    filename_replace = filename_2 + file_type
    src = get_file_from_directory(dirpath)
    dst = os.path.join(dirpath, filename_replace)
    os.rename(src, dst)
    return filename_replace


# 获取图片定位元素
def get_file_locator(filename):
    element = ('//*[@class="files_thumbnails fake no_list"]//h5[text()={0}{1}{2}]'.format('"', filename, '"'),)
    by = ('xpath',)
    locator = by + element
    return locator


def get_file_locator_and_path(dirpath, file_type='.jpg'):
    filename = modify_filename_and_return_filename(dirpath, file_type)  # 图片更名
    locator = get_file_locator(filename)  # 获取定位
    filepath = get_file_from_directory(dirpath)  # 获取更名后的图片路径
    return locator, filepath


def get_file_locator_and_path_without_modify_filename(dirpath):
    all_files = os.listdir(dirpath)  # 获取目录中的所有文件名称，得到一个列表
    random_file = random.choice(all_files)  # 从列表all_files中随机获取一个元素
    file_path = os.path.join(dirpath, random_file)  # 目录路径+文件名 = 完整的文件路径
    locator = get_file_locator(random_file)
    return locator, file_path


if __name__ == '__main__':
    dirpath = r"C:\Users\yyzz\Desktop\图片\area_bg\add"
    a = get_file_locator_and_path(dirpath, file_type='.mp4')
    print(a[0], a[1])
