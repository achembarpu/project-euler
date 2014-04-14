# Tools


import time


class Timer(object):
    """
    A Timer implementation, to easily time code-snippet execution
    Use as:
    with Timer():
        #code
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
