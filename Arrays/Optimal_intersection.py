# Problem: Intersection of Two Sorted Arrays (Optimal Two-Pointer Approach)
# Time Complexity: O(N1 + N2) — Single linear pass through both sorted arrays.
# Space Complexity: O(1) auxiliary space — In-place pointer traversal (excluding output list).
def intersection(arr1: list[int], arr2: list[int]) -> list[int]:

    i = 0
    j = 0

    inter = []
    while(i < len(arr1) and j < len(arr2)):
        if (arr1[i] < arr2[j]):
            i += 1
        elif (arr1[i] > arr2[j]):
            j += 1
        elif (arr1[i] == arr2[j]):
            inter.append(arr1[i])
            i += 1
            j += 1

    return inter


def main():
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr2 = [2, 3, 4, 4, 5, 11, 12]

    res = intersection(arr1, arr2)
    print(res)

if __name__ == "__main__":
    main()