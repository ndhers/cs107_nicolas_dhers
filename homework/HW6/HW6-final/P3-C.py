import matplotlib.pyplot as plt
from P3 import NaivePriorityQueue, HeapPriorityQueue, PythonHeapPriorityQueue, timeit


naive = timeit(pqclass=NaivePriorityQueue)
heap = timeit(pqclass=HeapPriorityQueue)
py_heap = timeit(pqclass=PythonHeapPriorityQueue)

ns = [10, 20, 50, 100, 200, 500]

plt.figure(figsize=(12, 9))
plt.plot(ns, naive, label="NaivePriorityQueue", color='blue')
plt.plot(ns, heap, label="HeapPriorityQueue", color='red')
plt.plot(ns, py_heap, label="PythonPriorityQueue", color='green')
plt.title("Performance Comparison of Three Priority Queues", fontsize=15)
plt.xlabel("Number of Merged Lists", fontsize=13)
plt.ylabel("Elapsed time in seconds", fontsize=13)
plt.legend(fontsize=12)
# plt.show()
plt.savefig('P3-C.png')
