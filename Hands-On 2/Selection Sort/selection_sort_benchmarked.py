import timeit
import random
import matplotlib.pyplot as plt
import psutil
import platform

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def benchmark_sort(arr_size, num_runs=100):
    numbers = [random.randint(1, 1000) for _ in range(arr_size)]
    def benchmark():
        return selection_sort(numbers.copy())
    
    time_taken = timeit.timeit(benchmark, number=num_runs) / num_runs
    return time_taken

def print_system_info():
    # Get system information
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
times = []

# Perform benchmarking for each array size
for size in array_sizes:
    time_taken = benchmark_sort(size)
    times.append(time_taken)
    print(f"Size: {size}, Time taken: {time_taken:.4f} seconds")

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(array_sizes, times, marker='o', linestyle='-', color='b')
plt.xlabel('Array Size')
plt.ylabel('Time Taken (seconds)')
plt.title('Time vs Array Size for Selection Sort')
plt.grid(True)
plt.show()
