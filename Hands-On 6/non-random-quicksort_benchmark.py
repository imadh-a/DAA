import matplotlib.pyplot as matplt
import timeit as t
import random as rand


def nonrandom_quicksort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    lesser = [x for x in array if x < pivot]
    equal = [x for x in array if x == pivot]
    greater = [x for x in array if x > pivot]
    return nonrandom_quicksort(lesser) + equal + nonrandom_quicksort(greater)

def bestcase_in(n):
    return list(range(1, n+1))

def worstcase_in(n):
    return list(range(n, 0, -1))

def average_in(n):
    return [rand.randint(1, 1000) for _ in range(n)]

def benchmark(sort_function, input_generator, sizes, repetitions):
    results = []
    for size in sizes:
        input_data = input_generator(size)
        time = t.timeit(lambda: sort_function(input_data.copy()), number=repetitions)
        results.append(time / repetitions)
    return results

sizes = [10, 100, 500, 1000, 2000]
repetitions = 10

bestcase_times = benchmark(nonrandom_quicksort, bestcase_in, sizes, repetitions)
worstcase_times = benchmark(nonrandom_quicksort, worstcase_in, sizes, repetitions)
averagecase_times = benchmark(nonrandom_quicksort, average_in, sizes, repetitions)

matplt.figure(facecolor='black')

matplt.plot(sizes, bestcase_times, label='Best Case', color='cyan')
matplt.plot(sizes, worstcase_times, label='Worst Case', color='magenta')
matplt.plot(sizes, averagecase_times, label='Average Case', color='yellow')

#matplt.gca().invert_yaxis()

matplt.xlabel('Input Size', color='white')
matplt.ylabel('Time (seconds)', color='white')
matplt.title('nonrandom_quicksort Benchmark', color='white')
matplt.legend()

matplt.tick_params(axis='x', colors='white')
matplt.tick_params(axis='y', colors='white')

matplt.show()
