# -*- coding: utf-8 -*-

import os
import sys
import argparse
import signal
import time
from multiprocessing import Process
from multiprocessing import Queue
from src.daemon import Daemon
from src.daemon import do_command
from src.process_pool import ProcessPool
from src.base_handler import BaseHandler

pid_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample.pid")
log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample.log")


class SampleDaemon(Daemon):
    def __init__(self):
        super(SampleDaemon, self).__init__(pid_path, stdout=log_file)
        self.process_pool = ProcessPool()

    def sigterm(self, signum, frame):
        self.terminate_process()

    def terminate_process(self):
        self.process_pool.terminate_process()

    def add_handler(self, handler, process_count, **kwargs):
        self.process_pool.add_handler(handler, process_count, **kwargs)

    def run(self):
        signal.signal(signal.SIGTERM, self.sigterm)
        self.process_pool.create_process()
        self.process_pool.start_process()
        self.process_pool.join_process()


class SampleHandler1(BaseHandler):
    def do_work(self):
        while not self.is_term:
            print("I am SampleHandler1 - pid:", os.getpid())
            time.sleep(5)


class SampleHandler2(BaseHandler):
    def do_work(self):
        while not self.is_term:
            print("I am SampleHandler2 - pid", os.getpid())
            time.sleep(5)

if __name__ == '__main__':
    daemon = SampleDaemon()
    daemon.add_handler(SampleHandler1, 1)
    daemon.add_handler(SampleHandler2, 2)

    operation = do_command()
    if operation == 'start':
        daemon.start()
    elif operation == 'restart':
        daemon.restart()
    elif operation == 'stop':
        daemon.stop()
    elif operation == 'status':
        pid = daemon.get_pid()
        if not pid:
            print("Daemon is not running;)")
        else:
            print("Daemon is running (PID: %d)" % pid)
    else:
        print("Invaild command")
    sys.exit(0)
