import timeit
import random
import matplotlib.pyplot as plt


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


def benchmark_sort(arr_size, num_runs=10):
    numbers = [random.randint(1, 1000) for _ in range(arr_size)]

    def benchmark():
        return insertion_sort(numbers.copy())

    time_taken = timeit.timeit(benchmark, number=num_runs) / num_runs
    return time_taken


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
plt.title('Time vs Array Size for Insertion Sort')
plt.grid(True)
plt.show()
