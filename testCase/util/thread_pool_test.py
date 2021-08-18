import threading
import unittest
from util.thread_pool import ThreadPool


class ThreadPoolTestCase(unittest.TestCase):

    def setUp(self):
        self.ThreadPool = ThreadPool()

    # 任务
    def task(self, taskId):
        thread_name = threading.current_thread().getName()
        print('工人【%s】正在处理任务【%d】：do something...' % (thread_name, taskId))

    def testReadInfo(self):
        pool = self.ThreadPool.thread_pool_init()
        for i in range(10):
            # 提交任务到池子(商会)里（它会自动分配给工人）
            pool.submit(self.task, i + 1)
