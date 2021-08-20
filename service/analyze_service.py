import os

import jieba
from util.write_txt import WriteTxt

from util.read_excel import ReadExcel


class AnalyzeService(object):
    file_path = os.getcwd() + '/data/excel'

    def __init__(self, file_path: None):
        self.file_path = file_path

    def analyze_search_word(self):
        for file in os.listdir(self.file_path):
            word_list = ReadExcel(file).read_excel()
            for word in word_list:
                cut_word_list = jieba.cut(word)
                for cut_word in cut_word_list:
                    WriteTxt.write_txt(cut_word)
