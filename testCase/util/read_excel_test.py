import os
import unittest
from util.read_excel import ReadData


class ReadDataTestCase(unittest.TestCase):

    def setUp(self):
        self.ReadData = ReadData(os.getcwd() + '/testCase/data/test.xlsx')

    def testReadInfo(self):
        self.assertTrue(self.ReadData.read_info(), list)
