import linecache


class ReadTxt(object):
    file_path = []
    position = 1
    file = None

    def __init__(self, file_path: [], file: None, position: 1):
        self.file_path = file_path
        self.file = file
        self.position = position

    # 获取文件位置的词
    def txt_word(self):
        if not self.file:
            return None
        word = linecache.getline(self.file, self.position)
        if word:
            return word
        else:
            return None

    # 获取文件位置的词进行比对统计
    def read_count(self, key_word):
        if not key_word:
            return 0
        count = 0
        for file in self.file_path:
            position = 1
            while True:
                word = linecache.getline(file, position)
                if word and key_word is word:
                    count = count + 1
                else:
                    break
                position = position + 1
        return count

    # 获取文件位置的词进行比对统计
    def read_split_count(self, key_word):
        if not key_word:
            return 0
        count = 0
        for file in self.file_path:
            position = 1
            while True:
                word = linecache.getline(file, position)
                if word and key_word is word:
                    word_info = word.split(sep=':')
                    if word_info[0] is key_word:
                        count = count + word_info[1]
                else:
                    break
                position = position + 1
        return count
