import unittest
from util.write_txt import WriteTxt


class WriteTxtTestCase(unittest.TestCase):

    def setUp(self):
        self.WriteTxt = WriteTxt()

    def testReadInfo(self):
        self.WriteTxt.write_txt()
