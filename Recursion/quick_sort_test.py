 quick_sort_test.py - verify corrected Quick Sort from notebook

def qs(arr, low, high):
    # QuickSort recursive function: sorts arr[low..high]
    if low < high:
        # partition returns an index 'p' such that items <= pivot are on left
        pIndex = f(arr, low, high)
        # Recursively sort left and right partitions (Hoare's partition returns p such that
        # left partition is low..p and right partition is p+1..high)
        qs(arr, low, pIndex)
        qs(arr, pIndex + 1, high)


def f(arr, low, high):
    # Hoare partition scheme implementation
    pivot = arr[low]
    i = low - 1
    j = high + 1
    while True:
        # Move i right until arr[i] >= pivot
        i += 1
        while arr[i] < pivot:
            i += 1
        # Move j left until arr[j] <= pivot
        j -= 1
        while arr[j] > pivot:
            j -= 1
        # If pointers have crossed, partitioning is done
        if i >= j:
            return j
        # Otherwise swap elements at i and j
        arr[i], arr[j] = arr[j], arr[i]


def main():
    arr = [2, 3, 1, 5, 7, 4, 9, 6]
    print("Original:", arr)
    qs(arr, 0, len(arr)-1)
    print("Sorted:", arr)

if __name__ == '__main__':
    main()
