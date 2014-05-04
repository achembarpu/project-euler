# Tools


import signal
import time

from src.py.custom import excepts


class Timer(object):
    """
    A Timer tool, to time code-snippet execution
    Use as:
    with Timer():
        # code
    """
    def __init__(self):
        self.start = 0.0
        self.end = 0.0
        self.interval = 0.0

    def __enter__(self):
        self.start = time.clock()

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start
        
        print "execution time = %s s" % (self.interval)


class Timeout(object):
    """
    A Timeout checker, to handle functions that may stall
    Use as:
    try:
        with Timeout(seconds):
            # code
    except TimeoutError:
        # handle it
    """
    def __init__(self, seconds=1):
        self.seconds = seconds
    
    def handle_timeout(self, *args):
        raise excepts.TimeoutError()
    
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)
    
    def __exit__(self, *args):
        signal.alarm(0)
