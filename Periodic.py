__author__ = 'xiongyi'
from threading import Timer, Lock


class Periodic(object):
    """
    A periodic task running in threading.Timers
    """

    def __init__(self, interval, function, *args, **kwargs):
        self._lock = Lock()
        self._timer = None
        self.function = function
        self.interval = interval
        self.args = args
        self.kwargs = kwargs
        self._stopped = True
        self.count = 0
        self.goal = 99999
        if kwargs.pop('autostart', True):
            self.start()

    def start(self, from_run=False):
        self._lock.acquire()
        if from_run or self._stopped:

            # if from_run and self._timer is not None:
            #     self._timer.join()
            self._stopped = False
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
        self._lock.release()
        self.count += 1
        if self.count >= self.goal:
            self.stop()

    def _run(self):
        self.start(from_run=True)
        try:
            self.function(*self.args, **self.kwargs)
        except Exception as e:
            self.stop()
            # print( "<p>Error: %s</p>" % str(e))
            raise e


    def stop(self):
        self._lock.acquire()
        self._stopped = True
        self._timer.cancel()
        self._lock.release()