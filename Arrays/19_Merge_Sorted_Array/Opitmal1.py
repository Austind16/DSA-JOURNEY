# Problem: Merge Two Sorted Arrays Without Extra Space (Optimal Pointer Swap Approach)
# Time Complexity: O(min(N, M) + N log N + M log M) — Swap pass + individual sorts.
# Space Complexity: O(1) auxiliary space — In-place array modification.
def merge_array(arr1: list[int], arr2: list[int]) -> list[int]:
    n = len(arr1)
    m = len(arr2)
    i = n - 1
    j = 0
    while i >= 0 and j < m:
        if arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]
            i -= 1
            j += 1 
        else:
            break

    arr1.sort()
    arr2.sort()

    return arr1, arr2
    

def main():
    arr1 = [1, 3, 5, 7]
    arr2 = [0, 2, 6, 8, 9]
    merge_array(arr1, arr2)
    print(arr1, arr2)

if __name__ == "__main__":
    main()