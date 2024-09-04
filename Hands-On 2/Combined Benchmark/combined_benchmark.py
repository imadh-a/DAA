import timeit
import random
import matplotlib.pyplot as plt
import psutil
import platform


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def benchmark_sort(sort_function, arr_size, num_runs=10):
    numbers = [random.randint(1, 1000) for _ in range(arr_size)]

    def benchmark():
        return sort_function(numbers.copy())

    time_taken = timeit.timeit(benchmark, number=num_runs) / num_runs
    return time_taken


def print_system_info():
    uname_info = platform.uname()
    cpu_info = psutil.cpu_freq()
    ram_info = psutil.virtual_memory()

    print(f"System: {uname_info.system} {uname_info.release} ({uname_info.version})")
    print(f"Machine: {uname_info.machine}")
    print(f"CPU: {uname_info.processor}")
    print(f"CPU Frequency: {cpu_info.current} MHz (Max: {cpu_info.max} MHz)")
    print(f"Total RAM: {ram_info.total / (1024 ** 3):.2f} GB")
    print(f"Available RAM: {ram_info.available / (1024 ** 3):.2f} GB")
    print(f"Used RAM: {ram_info.used / (1024 ** 3):.2f} GB")
    print(f"RAM Percentage: {ram_info.percent}%")


# Print system information
print_system_info()

# Define different array sizes
array_sizes = [5, 10, 20, 2000, 4000, 8000]

# Initialize dictionaries to store times
bubble_times = []
insertion_times = []
selection_times = []

# Perform benchmarking for each array size
for size in array_sizes:
    bubble_time = benchmark_sort(bubble_sort, size)
    insertion_time = benchmark_sort(insertion_sort, size)
    selection_time = benchmark_sort(selection_sort, size)

    bubble_times.append(bubble_time)
    insertion_times.append(insertion_time)
    selection_times.append(selection_time)

    print(f"Size: {size}")
    print(f"  Bubble Sort Time: {bubble_time:.4f} seconds")
    print(f"  Insertion Sort Time: {insertion_time:.4f} seconds")
    print(f"  Selection Sort Time: {selection_time:.4f} seconds")

# Plotting
plt.figure(figsize=(12, 8))
plt.plot(array_sizes, bubble_times, marker='o', linestyle='-', color='r', label='Bubble Sort')
plt.plot(array_sizes, insertion_times, marker='o', linestyle='-', color='b', label='Insertion Sort')
plt.plot(array_sizes, selection_times, marker='o', linestyle='-', color='g', label='Selection Sort')
plt.xlabel('Array Size')
plt.ylabel('Time Taken (seconds)')
plt.title('Time vs Array Size for Sorting Algorithms')
plt.legend()
plt.grid(True)
plt.show()
