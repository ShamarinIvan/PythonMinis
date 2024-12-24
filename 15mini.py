import threading
from time import time

task_queue = []
queue_lock = threading.Lock()

def matrix_power(matrix, power):
    size = len(matrix)
    result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]

    for _ in range(power):
        temp = [[0] * size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                temp[i][j] = sum(matrix[i][k] * result[k][j] for k in range(size))
        result = temp
    return result

def create_matrix(size, value):
    return [[value ** (i + j) for j in range(size)] for i in range(size)]

def producer(task_count):
    size = 4
    for _ in range(task_count):
        task = (size, 2, 3)
        with queue_lock:
            task_queue.append(task)
        size += 1

def consumer(consumer_id, results):
    while True:
        with queue_lock:
            if not task_queue:
                break
            task = task_queue.pop(0)

        size, value, times = task
        matrix = create_matrix(size, value)
        matrix = matrix_power(matrix, times)
        result = sum(sum(row) for row in matrix)
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
