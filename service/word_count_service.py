import os

from util.max_size import MaxSize
from util.read_txt import ReadTxt
from util.write_txt import WriteTxt


class WordCount(object):
    file_path = os.getcwd() + '/data/result'
    file_name = 'result_data'
    file_count = 4
    file_path_list = []

    def __init__(self, file_path: None, file_count: 5, file_name: None, file_path_list: None):
        if file_path:
            self.file_path = file_path
        self.file_count = file_count
        if file_name:
            self.file_name = file_name
        if file_path_list:
            self.file_path_list = file_path_list

    def first_word_count(self):
        # 获取解析出来最大的文件数
        maxSize = MaxSize.get_max_size(self.file_path)
        # 对数据进行拆分分组同时进行数量统计
        position = 1
        add_position = 0
        init_position = 1
        # 获取组合map,对文件进行分组处理
        group_map = dict()
        full_text_path = []
        while True:
            full_path = self.file_path + "/" + self.file_name + "_" + position + ".txt"
            full_text_path.insert(full_path)
            # 计算位置
            position = position + add_position
            group_map.setdefault(init_position, full_text_path)
            # 每5个文件进行数据处理
            if add_position == self.file_count:
                add_position = 0
                init_position = init_position + 1
                full_text_path.clear()
            # 计算弹出的位置
            if position > maxSize:
                break
        # 通过对组合map进行数据过滤,同事进行统计
        for key in group_map.keys():
            WordCount(file_path=os.getcwd() + '/data/result/count', file_path_list=group_map.get(key))

    # 唯一话统计数据
    def second_word_count(self):
        # 对当前文件数据进行去重
        for file in self.file_path_list:
            position = 1
            while True:
                word = ReadTxt(file=file, position=position).txt_word()
                if not word:
                    break
                one_count = word.split(sep=':')
                word_count = ReadTxt(file_path=self.file_path_list).read_count(count[0])
                count = word_count - one_count
                WriteTxt(txt_path=self.file_path).write_txt(word + ':' + count)
                position = position + 1

    # 分批统计数量
    def txt_word_count(self):
        # 对当前文件数据进行去重
        for file in self.file_path_list:
            position = 1
            while True:
                word = ReadTxt(file=file, position=position).txt_word()
                if not word:
                    break
                word_count = ReadTxt(file_path=self.file_path_list).read_count(word)
                WriteTxt(txt_path=self.file_path).write_txt(word + ':' + word_count)
                position = position + 1
