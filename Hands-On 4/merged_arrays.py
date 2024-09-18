class SortedArraysMerge:
    def merge(self, arr, left, middle, right):
        n1 = middle - left + 1
        n2 = right - middle

        left_array = arr[left:left + n1]
        right_array = arr[middle + 1:middle + 1 + n2]

        i = j = 0
        k = left

        while i < n1 and j < n2:
            if left_array[i] <= right_array[j]:
                arr[k] = left_array[i]
                i += 1
            else:
                arr[k] = right_array[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = left_array[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = right_array[j]
            j += 1
            k += 1

    def sort(self, arr, left, right):
        if left < right:
            middle = left + (right - left) // 2
            self.sort(arr, left, middle)
            self.sort(arr, middle + 1, right)
            self.merge(arr, left, middle, right)

    def sort_full(self, arr):
        self.sort(arr, 0, len(arr) - 1)

def main():
    K = int(input("Enter the number of Sorted Arrays:K = "))
    N = int(input("Enter the size of each array:N = "))

    one_d = []
    for i in range(K):
        print(f"Enter sorted elements for array{i+1}")
        array = [int(input()) for _ in range(N)]
        one_d.extend(array)

    ms = SortedArraysMerge()
    ms.sort_full(one_d)
    print("Sorted array:", one_d)

if __name__ == "__main__":
    main()
