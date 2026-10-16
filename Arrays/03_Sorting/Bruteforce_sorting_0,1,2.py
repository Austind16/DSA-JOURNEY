# Problem: Sort Colors / Sort an Array of 0s, 1s, and 2s (Brute Force - Quick Sort Approach)
# Time Complexity: O(N log N) Average Case | O(N^2) Worst Case
# Space Complexity: O(log N) — Call stack depth for recursion.
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

def merge(low, high, arr: list[int]):
    if low < high:
        p_index = partition(low, high, arr)

        merge(low, p_index - 1, arr)
        merge(p_index + 1, high, arr)

def main():
    arr = [0, 2, 2, 1, 0, 0, 1, 1, 2]
    merge(0, len(arr) - 1, arr)
    print(arr)

if __name__ == "__main__":
    main()