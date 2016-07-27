# -*- coding: utf-8 -*-
import signal


class BaseHandler():
    """
    A generic daemon class.
    A base process handler class

    Usage: subclass the BaseHandler class and override the do_work() method
    """
    def __init__(self):
        self.is_term = False

    def sigterm(self, signum, frame):
        self.is_term = True

    def run(self):
        signal.signal(signal.SIGTERM, self.sigterm)
        while self.is_term is False:
            self.do_work()

    def do_work(self):
        """
        You should override this method for handler logic
        """
        raise NotImplementedError("Subclasses must implement this function.")
