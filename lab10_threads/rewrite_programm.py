import urllib.request
import time
import threading
import os


urls = [
    'https://www.yandex.ru', 'https://www.google.com',
    'https://habrahabr.ru', 'https://www.python.org',
    'https://isocpp.org',
]


def read_url(urls):
    return [os.popen('ping ' + url).read() for url in urls]

start = time.time()
threads = [threading.Thread(target=read_url(url)) for url in urls]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print('c потоками: ', time.time() - start) 

start = time.time()
for url in urls:
    read_url(url)
print('без: ', time.time() - start)

'''
c потоками:  40.01757550239563
без:  188.15056991577148
'''

