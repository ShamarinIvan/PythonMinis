import threading
from queue import Queue
import numpy as np
from time import time

task_queue = Queue()
queue_lock = threading.Lock()

def producer(task_count):
    size = 2
    for _ in range(task_count):
        task = (size, 2, 3)
        with queue_lock:
            task_queue.put(task)
        size += 1 

def consumer(consumer_id, results):
    while True:
        with queue_lock:
            if task_queue.empty():
                break
            task = task_queue.get()
        
        size, value, times = task
        A = np.array([[value ** (i + j) for j in range(size)] for i in range(size)])
        A = np.linalg.matrix_power(A, times)
        result = np.sum(A)
        results[consumer_id] += result

def main(task_count=10, consumer_count=4):
    results = [0] * consumer_count
    threads = []

    producer_thread = threading.Thread(target=producer, args=(task_count,))
    producer_thread.start()
    producer_thread.join()

    for i in range(consumer_count):
        thread = threading.Thread(target=consumer, args=(i, results))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    total_result = sum(results)
    print(f"Consumers={consumer_count}, Result={total_result}")

if __name__ == "__main__":
    start_time = time()
    main(task_count=20, consumer_count=4)
    print(f"Execution Time: {time() - start_time:.10f}s")
