# Problem: Sort Colors / Dutch National Flag Algorithm (Optimal 3-Pointer Approach)
# Time Complexity: O(N) — Single-pass linear scan with 3 pointers (low, mid, high).
# Space Complexity: O(1) — In-place array modification using constant extra space.
def dutch_flag(arr: list[int]):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1

        elif arr[mid] == 1:
            mid += 1

        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

def main():
    arr = [0, 2, 2, 1, 0, 0, 1, 1, 2]
    dutch_flag(arr)
    print(arr)

if __name__ == "__main__":
    main()