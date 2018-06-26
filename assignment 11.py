#QUE1-
import threading
import time
from  threading import Thread
class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread. __init__(self)
        self.h = i

    def run(self):
        time.sleep(5)
        print("value send",self.h)
thread1 =  mythread(1)
thread1.start()

#QUE2
import threading
import time
from threading import Thread
class  histhread(threading.Thread):
    def __init__(self, i):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):
        print("no. is", self.h)
for i in range (10):
    thread1= histhread(i)
    thread1.start()
    time.sleep(1)

print ("active thread",+ i)

#QUE 3

import threading
import time
class herthread(threading.Thread):
    def __init__(self,value):
        threading.Thread.__init__(self)
        self.v=value
    def run(self):
        l = [2,4,6,8,10]
        for i in range (0,5):
            print(self.v[i])
            time.sleep(l[i])
thread1=herthread([1,2,3,4,5])
thread1.start()

#QUE4-

import threading
import math
from threading import Thread
class mythread (threading.Thread):
            def __init__(self, value):
                threading.Thread.__init__(self)
                self.v = value
            def run(self):
                print(math.factorial(self.v))
th1=mythread(5)
th1.start()





