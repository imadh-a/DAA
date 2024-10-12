import random as rand

def partitioning(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quickselect(arr, low, high, k):
    if low <= high:
        pivot_index = partitioning(arr, low, high)
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index < k:
            return quickselect(arr, pivot_index + 1, high, k)
        else:
            return quickselect(arr, low, pivot_index - 1, k)

def ith_order_statistic(arr, i):
    if i < 0 or i >= len(arr):
        return None
    return quickselect(arr, 0, len(arr) - 1, i)

if __name__ == '__main__':
    array = [rand.randint(0, 100) for i in range(10)] # random array with 10 elements between [0-100]
    i = rand.randint(0, len(array) - 1) # random selection of i

    print("Array:", array)
    print(f"Search for {i+1}th order statistic:")
    print(f"{i+1}th order statistic:", ith_order_statistic(array, i))

    # Validation of the ith order statistic
    sorted_array = array.copy()
    sorted_array.sort()
    print(f"Actual {i+1}th order statistic: ", sorted_array[i])
