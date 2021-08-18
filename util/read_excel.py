import os
import xlrd
import re


class ReadData(object):
    file_path = os.getcwd() + '/data'
    sheet_list = [1]
    header_row = 1
    data_cell = 1
    read_size = 500
    file_format = ['xls', 'xlsx']

    def __init__(self, file, header_raw: 1, data_cell: 1, sheet_list: [1], read_size: 500):
        self.file_path = file
        self.data_cell = data_cell
        self.header_row = header_raw
        self.sheet_list = sheet_list
        self.read_size = read_size

    # 读取需要解析的文件
    def read_info(self):
        if (len(filter(lambda x: re.search(x, self.file_path), self.file_format)) > 0):
            print("文件格式错误，请上传正确的文件")
            return
        if (os.path.getsize(self.file_path) > self.read_size):
            print("文件太大，无法处理")
            return
        excel = xlrd.open_workbook(self.file_path, encoding_override='utf-8')
        all_sheet = excel.sheets()
        list_data = []
        for i in range(len(all_sheet)):
            if i in all_sheet:
                sheet = excel.sheet_by_index(i)
                list_data.insert(sheet.col_values(self.data_cell))
        return list_data
