from concurrent.futures.thread import ThreadPoolExecutor


class ThreadPool(object):
    max_work = 5
    thread_name_prefix = 'thread'

    def __init__(self, max_work: 5, thread_name_prefix: 'thread_name_prefix'):
        self.max_work = max_work
        self.thread_name_prefix = thread_name_prefix

    def thread_pool_init(self):
        return ThreadPoolExecutor(max_workers=self.max_work, thread_name_prefix=self.thread_name_prefix)

