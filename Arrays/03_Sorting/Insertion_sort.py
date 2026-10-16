# Problem: Insertion Sort
# Time Complexity: O(N) Best Case (Already Sorted) | O(N^2) Average & Worst Case
# Space Complexity: O(1) — In-place sorting using constant auxiliary space.
def insertion_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr

def main():
    arr = [6, 5, 2, 1, 3]
    ans = insertion_sort(arr)
    print(ans)

if __name__ == "__main__":
    main()