# -*- coding: utf-8 -*-

from multiprocessing import Process

class ProcessPool():
    """
    Management process pool class

    Usage: Create a process in the following order
        - 1. add_handler method
        - 2. create_process method
        - 3. start_process method
        - 4. join_process method
    Usage: Terminate processes as follows
        - 1. terminate_process method
    """
    def __init__(self):
        self.proc = list()
        self.index = 0


    def add_handler(self, handler, process_count, **kwargs):
        """
        Add process handler function
        """
        handlers = [handler(**kwargs) for i in range(process_count)]
        self.proc.append({'handler': handlers, 'process_count': process_count})
        self.index += 1


    def create_process(self):
        """
        create process based on the registered handler
        """
        for idx in range(self.index):
            process = [Process(target=self.proc[idx]['handler'][i].run) for i in range(self.proc[idx]['process_count'])]
            self.proc[idx].update({'process': process})


    def start_process(self):
        """
        start process
        """
        for idx in range(self.index):
            for p in self.proc[idx]['process']:
                p.start()


    def join_process(self):
        """
        join process
        """
        for idx in range(self.index):
            for p in self.proc[idx]['process']:
                p.join()


    def terminate_process(self):
        """
        terminate process
        """
        for idx in range(self.index):
            for p in self.proc[self.index-idx-1]['process']:
                if p.is_alive():
                    p.terminate()
