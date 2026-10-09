def partition(low, high, arr: list[int]) -> int:
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while arr[i] <= pivot and i < high:
            i += 1

        while arr[j] > pivot and j > low:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]

    return j

def quick_sort(low, high, arr: list[int]):
    if low < high:
        p_index = partition(low, high, arr)

        quick_sort(low, p_index - 1, arr)
        quick_sort(p_index + 1, high, arr)

def main():
    arr = [4, 3, 5, 1, 7, 2, 9, 6]
    quick_sort(0, len(arr) - 1, arr)
    print(arr)

if __name__ == "__main__":
    main()