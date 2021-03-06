"""
# 1. Write the method that return the number of threads currently in execution.
# Also prepare the method that will be executed with threads and run during the first method counting.
"""

import threading
from time import sleep


def func1():
    for i in range(5):
        print(f"from first thread: {i}")
        sleep(0.5)


def func2():
    for i in range(5):
        print(f"from second thread: {i}")
        sleep(1)


th1 = threading.Thread(target=func1, name="func1")
th2 = threading.Thread(target=func2, name="func2")
th1.start()
th2.start()
while threading.activeCount() != 1:
    print(f"\n\nNow {threading.activeCount()} active Threads\n")
    sleep(2)
