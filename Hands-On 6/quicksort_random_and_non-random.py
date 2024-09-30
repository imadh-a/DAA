import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
#quicksort main
def quicksort(arr, low, high):
    if low < high: 
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def quicksort_random(arr, low, high):
    if low < high:
        pivot = random.randint(low, high)
        arr[pivot], arr[high] = arr[high], arr[pivot]
        pi = partition(arr, low, high)
        quicksort_random(arr, low, pi - 1)
        quicksort_random(arr, pi + 1, high)

# Wrapper functions for easier use
def quicksort_wrapper(arr):
    quicksort(arr[:], 0, len(arr) - 1)
    return arr

def quicksort_random_wrapper(arr):
    quicksort_random(arr[:], 0, len(arr) - 1)
    return arr

# Test the implementations
if __name__ == "__main__":
    test_arr = [3, 6, 8, 10, 1, 2, 1]
    print("Original array:", test_arr)
    print("Sorted array (non-random pivot):", quicksort_wrapper(test_arr))
    print("Sorted array (random pivot):", quicksort_random_wrapper(test_arr))
