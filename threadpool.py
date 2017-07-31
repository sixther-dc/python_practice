# coding=utf-8

from multiprocessing.pool import ThreadPool
import time

def touch_the_file(n):
    filename='temp' + n
    open(filename,'w')

pool=ThreadPool(100)
for i in range(1,50):
    #pool.apply_async(touch_the_file,(str(i),))
    pool.apply(touch_the_file,(str(i),))
#pool.close()
#pool.join()
#time.sleep(10)      由于apply_async是异步的,所以需要等到子线程退出完再退出主线程才能保证所有子线程全部执行完毕, 也使用apply同步执行。
#print async_result.get()

