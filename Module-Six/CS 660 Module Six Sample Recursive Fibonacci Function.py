import threading 
  
def fibonacci(n,thread_id=None): 
    print(f"Calculating fibonacci({n}) in thread {thread_id}")
    if n < 0: 
        raise ValueError("Fibonacci is not defined for negative numbers") 
    if n == 0: 
        return 0 
    elif n == 1: 
        return 1 
    return fibonacci(n - 1, thread_id) + fibonacci(n - 2, thread_id) 
  
# Multithreaded scenario 
def worker(thread_id, n): 
    print(f"Thread {thread_id} entered worker function")
    result = fibonacci(n, thread_id) 
    print(f"Thread {thread_id}: fibonacci({n}) = {result}") 
  
# Create multiple threads calling fibonacci(2) 
thread1 = threading.Thread(target=worker, args=(1, 2)) 
thread2 = threading.Thread(target=worker, args=(2, 2)) 
thread3 = threading.Thread(target=worker, args=(3, 2)) 

print("Starting threads to calculate fibonacci(2) concurrently...") 
thread1.start() 
thread2.start() 
thread3.start() 
thread1.join() 
print("Thread 1 finished")
thread2.join() 
print("Thread 2 finished")
thread3.join()
print("Thread 3 finished")