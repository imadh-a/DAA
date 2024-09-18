def remove_duplicates(sorted_array):
    if not sorted_array:
        return 0  # Return 0 if the array is empty

    # Initialize the unique index
    unique_index = 0

    # Start from the second element and compare with the previous one
    for i in range(1, len(sorted_array)):
        if sorted_array[i] != sorted_array[unique_index]:
            # Move unique_index forward and update the array
            unique_index += 1
            sorted_array[unique_index] = sorted_array[i]

    # Return the length of the array with unique elements
    return unique_index + 1


def main():
    # Get the size of the array from the user
    while True:
        try:
            size = int(input("Enter the size of the array:N = "))
            if size <= 0:
                print("Size must be a positive integer. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Initialize an empty array with the user-defined size
    sorted_array = []

    # Get array elements from the user
    print(f"Enter up to {size} elements")
    while len(sorted_array) < size:
        try:
            elements = input(f"Enter {size - len(sorted_array)} elements with spaces: ")
            elements = list(map(int, elements.split()))

            if len(elements) > (size - len(sorted_array)):
                print(f"Too many elements. Please enter up to {size - len(sorted_array)} elements.")
                continue

            sorted_array.extend(elements)

            # Check if the array has reached the defined size
            if len(sorted_array) >= size:
                break
        except ValueError:
            print("Invalid input. Please enter valid integers.")

    # Ensure the array is sorted
    sorted_array.sort()

    # Remove duplicates
    new_length = remove_duplicates(sorted_array)

    # Display the result
    print("Array after removing duplicates:", sorted_array[:new_length])
    print("New length of the array:", new_length)


if __name__ == "__main__":
    main()