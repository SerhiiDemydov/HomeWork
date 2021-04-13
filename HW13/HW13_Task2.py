"""
2. Print current date by using 2 threads.
#1. Define a subclass using Thread class.
#2. Instantiate the subclass and trigger the thread.
"""

import threading
from time import sleep
from datetime import datetime


class RealTime(threading.Thread):
    def __init__(self, limit, name):
        threading.Thread.__init__(self)
        self.limit = limit
        self.name = name

    def run(self):
        for i in range(self.limit):
            print(f"Date and time: {datetime.now()} in {self.name}")
            sleep(2)


real_time1 = RealTime(5,"Thread1")
real_time2 = RealTime(5,"Thread2")

real_time1.start()
real_time2.start()

real_time1.join()
real_time2.join()
