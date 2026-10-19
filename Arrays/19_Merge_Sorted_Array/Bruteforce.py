# Problem: Merge Two Sorted Arrays Without Extra Space (Brute Force Approach)
# Time Complexity: O(N + M) — Linear merging and re-assignment pass.
# Space Complexity: O(N + M) — Auxiliary array `arr3` used to store merged elements.
def merge_array(arr1: list[int], arr2: list[int]) -> list[int]:
    n = len(arr1)
    m = len(arr2)
    i = 0
    j = 0
    arr3 = []

    while i < n and j < m:
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1

    while i < n:
        arr3.append(arr1[i])
        i += 1

    while j < m:
        arr3.append(arr2[j])
        j += 1

    for i in range(0, len(arr3)):
        if i < n:
            arr1[i] = arr3[i]
        else:
            arr2[i - n] = arr3[i]

    return arr1, arr2

def main():
    arr1 = [1, 3, 5, 7]
    arr2 = [0, 2, 6, 8, 9]
    merge_array(arr1, arr2)
    print(arr1, arr2)

if __name__ == "__main__":
    main()