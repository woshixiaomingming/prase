import os


class MaxSize(object):

    txt_path = os.getcwd() + '/data/result'

    def __init__(self, txt_path: os.getcwd() + '/data/result'):
        self.txt_path = txt_path

    def get_max_size(self):
        maxSize = 1
        # 获取最大的文件
        for file in os.listdir(self.txt_path):
            if os.path.splitext(file)[1] == 'txt':
                size = os.path.splitext(file)[0].split(self.file_name)[1]
                if size > maxSize and os.path.getsize(file) < self.file_size_limit:
                    maxSize = size
        return maxSize
