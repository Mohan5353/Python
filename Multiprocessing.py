from multiprocessing import Process, Queue
import numpy.random as npr
import time

# import pandas as pd

dataset = npr.randint(0, 100000000, size=100000000)
# df = pd.DataFrame(dataset)
# df.to_excel("1.xlsx")

q = Queue()


def mean(start, end):
    _sum = 0
    for i in range(start, end):
        _sum += dataset[i]

    q.put(_sum / (end - start))


if __name__ == "__main__":
    p1 = Process(target=mean, args=(0, 50000000))
    p2 = Process(target=mean, args=(50000000, 100000000))
    # p3 = Process(target=mean, args=(0, 100000000))
    s_time = time.time()
    p1.start()
    p2.start()
    # p3.start()
    p1.join()
    p2.join()
    # p3.join()
    avg2 = 0
    while not q.empty():
        avg2 += q.get()
    avg2 /= 2
    e_time = time.time()
    print(e_time - s_time)
    time.sleep(3)
