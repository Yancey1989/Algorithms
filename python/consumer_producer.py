#-*- coding:utf-8 -*-

import Queue
import threading
import time
import json
import sys
import signal
import random
reload( sys )
sys.setdefaultencoding('utf-8')

class Enum(set):
    def __getattr__(self, name):
        if name in self:
            return name
        else:
            raise AttributeError
State = Enum(['NORMAL', 'UPDATE', 'STOP'])

engine_do = True
def handler(signum, frame):
    print 'receive signal: %s' % signum
    global engine_do
    engine_do = False

signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTERM, handler)

class Consumer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.do = True

    def stop(self):
        self.do = False
        print 'change consumer.do to False'
    
    def run(self):
        print 'Create new consumer thread, id: %s' % self.ident
        while self.do:
            messages = []
            result = []
            msg = random.randint(0,100)
            self.queue.put(msg)
        print 'Consumer thread will exit.'
        
class Producer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.msgs = Queue.Queue()
        self.state = State.NORMAL
        self.do = True

    def stop(self):
        self.do = False
        self.state = State.STOP

    def run(self):
        while self.do:
            if self.state == State.NORMAL:
                if not self.queue.empty():
                    data = self.queue.get()
                    print 'Producer get data: %s' % data
                else:
                    print 'data queue is empty, sleep 5 seconds.'
                    time.sleep(5)
            elif self.state == State.STOP:
                while not self.queue.empty():
                    data = self.queue.get()
                    print 'Producer get data: %s' % data
        print 'Producer thread will exit.'

class Engine():
    def __init__(self):
        # 在获取所有的topic并初始化连接
        # 初始化消费Queue中数据的线程
        self.queue = Queue.Queue()
        self.threads_consumer = []
        self.threads_producer = []


    def run(self):
        # 启动Consumer线程
        for i in xrange(10):
            consumer = Consumer(self.queue)
            consumer.start()
            self.threads_consumer.append(consumer)
        producer = Producer(self.queue)
        self.threads_producer.append(producer)
        producer.start()
        while True:
            time.sleep(5)
            print engine_do
            if not engine_do:
                print 'engine will exit...'
                print 'first stop consumer threads'
                for consumer in self.threads_consumer:
                    consumer.stop()
                for consumer in self.threads_consumer:
                    consumer.join()
                print 'all consumer threads are done.'
                print 'second stop producer threads...'
                for producer in self.threads_producer:
                    producer.stop()
                for producer in self.threads_producer:
                    producer.join()
                print 'all producer threads are done.'
                break
        print 'All threads are not alive, main thread will exit.'
        return 

if __name__=='__main__':
    engine = Engine()
    engine.run()
