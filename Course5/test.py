import itertools
import threading
import time
import sys


def the_process_function(foo):
    time.sleep(foo)


def animated_loading():
    chars = "/—\|"
    for char in chars:
        sys.stdout.write('\r'+'loading...'+char)
        time.sleep(.1)
        sys.stdout.flush()


foo = [10]
the_process = threading.Thread(name='process', target=the_process_function, args = foo)

the_process.start()


while the_process.isAlive():
    animated_loading()
