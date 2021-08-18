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

    def word_count (self):
        # 获取解析出来最大的文件数
        maxSize = MaxSize.get_max_size(self.file_path)
        # 对数据进行拆分分组同时进行数量统计以二分法进行统计
        pool = ThreadPool.thread_pool_init()
        init_position =  1



