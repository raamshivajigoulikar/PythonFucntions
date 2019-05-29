#Threads in python can be created by threading package.
#start is the method to start the thread

#Without creating any class
from threading import *
def display():
    print("The current thread here is:",current_thread().getName())

t=Thread(target=display)
print("The current thread here is outside:",current_thread().getName())
t.start()

from threading import *
def display():
    for i in range(10):
        print('Child Thread')

t=Thread(target=display)
t.start()
for j in range(10):
    print('Main Thread')


#Creating threads by extending Thread class.
from threading import *
class MyThread(Thread):
    def run(self):#predefined method name in Thread overriding here
        for i in range(10):
            print('My Child Thread-1')

t=MyThread()
t.start()
for i in range(10):
    print("Main Thread")

#Creating threads without extending Thread class.
from threading import *
class Test:
    def display(self):
        for i in range(10):
            print('My Child Thread-1')

obj=Test()
t=Thread(target=obj.display)
t.start()
for i in range(10):
    print("Main Thread")
