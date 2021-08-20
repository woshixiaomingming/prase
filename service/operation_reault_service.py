import os

from service.analyze_service import AnalyzeService
from service.word_count_service import WordCount
from util.read_txt import ReadTxt


class OperationResult(object):

    file=None

    def __init__(self, file):
        self.file = file

    def operation_result(self):
        AnalyzeService.analyze_search_word()
        WordCount(file_path=os.getcwd() + '/data/result/first').first_word_count()
        WordCount(file_path=os.getcwd() + '/data/result/second').second_word_count()

    def order_by(self):
        result = []
        count = []
        for file in os.listdir(os.getcwd() + '/data/result/second'):
            word = ReadTxt(file=file).txt_word()
            count = word.split(":")

