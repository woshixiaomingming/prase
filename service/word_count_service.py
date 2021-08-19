import os
from util.max_size import MaxSize
from util.thread_pool import ThreadPool


class WordCount(object):
    file_path = os.getcwd() + '/data/result'
    file_name = 'result_data'
    file_count = 5

    def __init__(self, file_path: os.getcwd() + '/data/result', file_count: 5, file_name: 'result_data'):
        self.file_path = file_path
        self.file_count = file_count
        self.file_name = file_name

    def word_count(self):
        # 获取解析出来最大的文件数
        maxSize = MaxSize.get_max_size(self.file_path)
        # 对数据进行拆分分组同时进行数量统计以二分法进行统计
        pool = ThreadPool.thread_pool_init()
        position = 1
        add_position = 0
        init_position = 1
        # 获取组合map
        group_map = dict()
        full_text_path = []
        while True:
            full_path = self.file_path + "/" + self.file_name + "_" + position + ".txt"
            full_text_path.insert(full_path)
            # 计算位置
            position = position + add_position
            group_map.setdefault(init_position, full_text_path)
            # 每5个文件进行数据处理
            if add_position == 4:
                add_position = 0
                init_position = init_position + 1
                full_text_path.clear()
            # 计算弹出的位置
            if position > maxSize:
                break
        # 通过对组合map进行数据过滤
        for key in group_map.keys():
            for path in group_map.get(key):
                return

    def txt_word_count (self, file_path_list: []):
        # 对当前文件数据进行去重
        return
