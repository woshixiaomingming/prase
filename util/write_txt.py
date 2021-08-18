import os
from util.max_size import MaxSize


class WriteTxt(object):

    txt_path = os.getcwd() + '/data/result'
    file_name = 'result_data'
    file_size_limit = 500 * 1048576

    def __init__(self, txt_path: os.getcwd() + '/data/result', file_name: 'result_data',
                 file_size_limit: 500 * 1048576):
        self.txt_path = txt_path
        self.file_name = file_name
        self.file_size_limit = file_size_limit

    # 保存解析后的数据到指定目录下
    def write_txt(self, key_word):
        if not os.path.exists(self.txt_path):
            os.mkdir(self.txt_path)

        full_path = self.txt_path + "/" + self.file_name + "_" + MaxSize.get_max_size() + '.txt'
        file = open(full_path, 'a')
        file.write(key_word + '\n')
        file.close()
