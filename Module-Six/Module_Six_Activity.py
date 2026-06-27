import threading
import random

lock = threading.Lock()  # lock to synchronize access to shared objects dictionary

objects = {i: None for i in range(100)}  # global dictionary to simulate objects in memory of size 100, initially all set to None (fully unallocated memory)


# create a dictionary of objects with random in use status (0 or 1)
def create_objects(n=10,thread_id=0):
    with lock:
        print(f"Thread {thread_id}: Inside function for creating dictionary of objects...")
        for i in range(n):
            key = random.randint(0, 99)  # random key between 0 and 99
            if objects[key] is None:  # only create object if memory unallocated
                objects[key] = random.randint(0, 1)
        print(f"Thread {thread_id}: Finished creating objects.")


# simulate object lifecycle by randomly marking objects as in use or not in use
def sim_object_lifecycle(objects, thread_id):
    with lock:
        key = random.randint(0, 99)  # random key between 0 and 99
        if objects[key] is not None:  # only simulate lifecycle if memory currently holds an object
            objects[key] = random.randint(0, 1)

# implement mark and sweep algorithm to clean up unused objects
def mark_and_sweep(objects, thread_id):
    with lock:
        print(f"Thread {thread_id}: Performing mark and sweep algorithm...")
        marked_in_use = []
        for key, is_used in objects.items():
            if is_used == 1:
                marked_in_use.append(key)
        print(f"Thread {thread_id}: Marked {len(marked_in_use)} objects as in use")
        for key, _ in list(objects.items()):
            if key not in marked_in_use and objects[key] is not None:
                objects[key] = None  # simulate memory cleanup by setting to None
        print(f"Thread {thread_id}: Completed mark and sweep.")

def print_memory_usage(thread_id):
    with lock:
        in_use = len([k for k, v in objects.items() if v is not None])
        print(f"Thread {thread_id}: Current memory allocated: {in_use} out of {len(objects)} ({in_use/len(objects)*100:.2f}%)")


# worker function to create objects, simulate lifecycle, and perform mark and sweep for each thread
def worker(thread_id, n=10):
    create_objects(n=n,thread_id=thread_id)
    print_memory_usage(thread_id)

    for i in range(n):
        sim_object_lifecycle(objects, thread_id=thread_id)

    mark_and_sweep(objects, thread_id=thread_id)
    print_memory_usage(thread_id)


# print initial memory usage before any threads start
print_memory_usage(thread_id=0)   

# Create and run multiple threads
thread1 = threading.Thread(target=worker, args=(1, 15))
thread2 = threading.Thread(target=worker, args=(2, 20))
thread3 = threading.Thread(target=worker, args=(3, 25))

print("Thread 1 is starting...")
thread1.start()
print("Thread 2 is starting...")
thread2.start()
print("Thread 3 is starting...")
thread3.start()

thread1.join()
print("Thread 1 has completed.")
thread2.join()
print("Thread 2 has completed.")
thread3.join()
print("Thread 3 has completed.")

print("All threads have completed.")