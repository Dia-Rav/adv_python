import threading
import random
import time
import sys  

def check_ip (k):
    global length 
    global N
    global array
    global sums
    #разбиение массива на N кусочков
    n = round(length/N * (k+1))
    sum = 0
    if n > length:
        n = length
    for i in range (round(length/N * (k)), n):
        sum+= array[i]
    sums += sum

sums = 0
array = [3, 9, 10, 3, 4, 5, 22, 4, 5, 6, 8, 11, 12, 3, 0, 23, 14, 65, 23, 90, 0, 9, 4, 5, 6, 2, 48, 9, 2, 1, 4, 2, 34, 54, 2]
length = len(array)
for N in range (1, 20):
    sums = 0
    start_time = time.time()
    #запускаем N потоков
    threads = [threading.Thread(target=check_ip(k)) for k in range(N)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()
    timer = - start_time + end_time
    print (round (timer, 4))
'''
Вывод для разного количества потоков:
0.011
0.003
0.003
0.005
0.006
0.007
0.008
0.01
0.011
0.012
0.013
0.014
0.015
0.0185
0.0189
0.017
0.018
0.017
0.0199
'''
