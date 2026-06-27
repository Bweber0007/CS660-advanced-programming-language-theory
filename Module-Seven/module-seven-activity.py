import time
import random
import gc
import heapq
import tracemalloc
from memory_profiler import memory_usage

#########################################################################
# Quick Sort Implementation
#########################################################################

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    left = []
    middle = []
    right = []
    pivot = arr[len(arr) // 2]

    for value in arr:
        if value < pivot:
            left.append(value)
        elif value > pivot:
            right.append(value)
        else:
            middle.append(value)

    return quicksort(left) + middle + quicksort(right)


#########################################################################
# Merge Sort Implementations
#########################################################################

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    result_append = result.append  # Local variable for faster access
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result_append(left[i])
            i += 1
        else:
            result_append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort_fast(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    # Pre-allocate a single auxiliary array to prevent memory thrashing
    aux = arr[:]
    
    def _merge_sort(source, dest, low, high):
        if high - low <= 1:
            return
        
        mid = (low + high) // 2
        
        # Ping-pong array roles to eliminate copying data back and forth
        _merge_sort(dest, source, low, mid)
        _merge_sort(dest, source, mid, high)
        
        # Merge pointers
        i, j= low, mid
        k = low
        
        # Tight loop: Only evaluates two index boundaries
        while i < mid and j < high:
            if source[i] <= source[j]:
                dest[k] = source[i]
                i += 1
            else:
                dest[k] = source[j]
                j += 1
            k += 1
            
        # Fast slice copy for the remaining elements of the unfinished side
        if i < mid:
            dest[k:high] = source[i:mid]
        else:
            dest[k:high] = source[j:high]

    _merge_sort(aux, arr, 0, n)
    return arr

#########################################################################
# Heap Sort Implementations
#########################################################################

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

def recursive_heap_sort(arr):
    n = len(arr)

    # Phase 1: Build a max heap
    # Start from the last non-leaf node and move up to the root
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Phase 2: One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap root with last element
        heapify(arr, i, 0)  # restore heap property on reduced heap

def iterative_heap_sort(arr):
    n = len(arr)

    # Step 1: Build Max Heap using Floyd's algorithm (Bottom-up sift down)
    for i in range(n // 2 - 1, -1, -1):
        # Inlined sift-down loop for performance
        parent = i
        while True:
            child = 2 * parent + 1
            if child >= n:
                break
            # Check if right child exists and is larger than left child
            if child + 1 < n and arr[child] < arr[child + 1]:
                child += 1
            # If parent is larger than largest child, heap property is valid
            if arr[parent] >= arr[child]:
                break
            # Swap parent and child
            arr[parent], arr[child] = arr[child], arr[parent]
            parent = child

    # Step 2: Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root to the end of the array
        arr[0], arr[i] = arr[i], arr[0]
        
        # Sift down the new root element through the reduced heap
        parent = 0
        while True:
            child = 2 * parent + 1
            if child >= i:
                break
            if child + 1 < i and arr[child] < arr[child + 1]:
                child += 1
            if arr[parent] >= arr[child]:
                break
            arr[parent], arr[child] = arr[child], arr[parent]
            parent = child
            
    return arr


def heapq_heap_sort(iterable):
    # Copying to a list to handle any iterable input
    h = list(iterable)
    heapq.heapify(h) # O(N) linear time heap construction
    return [heapq.heappop(h) for _ in range(len(h))] # O(N log N) extraction


###########################################################################
# Regular Sort Implementation
###########################################################################

def regular_sort(arr):
    return sorted(arr)


#########################################################################
# Performance Measurement
#########################################################################

def measure_time_and_memory(sort_function, arr, iterations=3):
    total_time = 0
    peak_traced_peak = 0

    for _ in range(iterations):
        # record time taken for sorting
        gc.collect()
        arr_copy_time = arr.copy()

        start_time = time.perf_counter()
        sort_function(arr_copy_time)
        end_time = time.perf_counter()
        total_time += end_time - start_time

        # record memory usage using tracemalloc
        gc.collect()
        arr_copy_trace = arr.copy()

        tracemalloc.start()
        sort_function(arr_copy_trace)
        _ , traced_peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        traced_peak_mb = traced_peak / 10 **6  # Convert bytes to MB
        peak_traced_peak = max(peak_traced_peak, traced_peak_mb)

    print(f"Time Taken: {total_time / iterations:.3f} seconds")
    print(f"Peak Memory Allocation: {peak_traced_peak:.5f} MB")

if __name__ == "__main__":
    data = [random.randint(1, 1000) for _ in range(100000)]  # Generate a list of 100000 random integers
    
    print("Measuring Quick Sort:")
    measure_time_and_memory(quicksort, data)
    
    print("\nMeasuring Standard Merge Sort:")
    measure_time_and_memory(merge_sort, data)

    print("\nMeasuring Speed-Optimized Merge Sort:")
    measure_time_and_memory(merge_sort_fast, data)

    print("\nMeasuring Recursive Heap Sort:")
    measure_time_and_memory(recursive_heap_sort, data)

    print("\nMeasuring Iterative Heap Sort:")
    measure_time_and_memory(iterative_heap_sort, data)

    print("\nMeasuring Heapq Heap Sort:")
    measure_time_and_memory(heapq_heap_sort, data)

    print("\nMeasuring Regular Sort:")
    measure_time_and_memory(regular_sort, data)
