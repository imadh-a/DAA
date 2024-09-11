import timeit
import matplotlib.pyplot as plt

# Redefining the function and input sizes
def calc_x(n):
    x = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            x = x + 1
    return x

# Benchmarking the function
n_values = [1, 2, 3, 10, 100, 500, 1000, 5000, 10000, 20000]
exec_times = [timeit.timeit(lambda: calc_x(n), number=1) for n in n_values]

# Printing the execution times
for n, execution_time in zip(n_values, exec_times):
    print(f"For n={n}, Execution Time: {execution_time:.4f} seconds")

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.plot(n_values, exec_times, marker='o', linestyle='-', color='r')
plt.title("Execution Time vs Input Size (n) for calc_x")
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.grid(True)
plt.xscale("log")
plt.yscale("log")
plt.show()
