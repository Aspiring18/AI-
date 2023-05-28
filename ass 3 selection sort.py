def greedy_selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        # Find the index of the smallest element in the unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the smallest element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Example usage
num_elements = int(input("Enter the number of elements: "))
arr = []
for _ in range(num_elements):
    element = int(input("Enter an element: "))
    arr.append(element)

sorted_arr = greedy_selection_sort(arr)
print("Sorted array:", sorted_arr)
