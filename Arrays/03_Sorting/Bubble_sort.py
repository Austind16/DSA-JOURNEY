# Problem: Bubble Sort (Optimized with Swapped Flag)
# Time Complexity: O(N) Best Case (Already Sorted) | O(N^2) Average & Worst Case
# Space Complexity: O(1) — In-place sorting using constant extra space.
def bubble_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr

def main():
    arr = [6, 5, 2, 1, 3]
    ans = bubble_sort(arr)
    print(ans)

if __name__ == "__main__":
    main()