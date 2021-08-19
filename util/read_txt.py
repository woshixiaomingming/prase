import os


class ReadTxt (object):

    txt_path = os.getcwd() + '/data/result'
    file_name = 'result_data'

    def __init__(self, txt_path: os.getcwd() + '/data/result', file_name: 'result_data'):
        self.txt_path = txt_path
        self.file_name = file_name

    def read_info (self, ):
