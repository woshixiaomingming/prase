import unittest
from util.max_size import MaxSize


class MaxSizeTestCase(unittest.TestCase):

    def setUp(self):
        self.MaxSize = MaxSize()

    def testReadInfo(self):
        self.MaxSize.get_max_size()
