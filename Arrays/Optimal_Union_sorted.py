# Problem: Union of Two Sorted Arrays (Optimal Two Pointer Approach)
# Time Complexity: O(N1 + N2) — Single traversal through both arrays.
# Space Complexity: O(N1 + N2) — In worst-case, union holds all unique elements from both arrays
def union_sorted(union, arr1: list[int], arr2: list[int]) -> list[int]:
    n1 = len(arr1)
    n2 = len(arr2)
    i = 0
    j = 0

    while(i < n1 and j < n2):
        if(arr1[i] <= arr2[j]):
            if (len(union) == 0 or (union[-1] != arr1[i])):
                union.append(arr1[i])
            i += 1
        else:
            if (len(union) == 0 or (union[-1] != arr2[j])):
                union.append(arr2[j])
            j += 1

    while i < n1:
        if len(union) == 0 or union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    while j < n2:
        if len(union) == 0 or union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    return union

def main():
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr2 = [2, 3, 4, 4, 5, 11, 12]
    union = []
    union_sorted(union, arr1, arr2)

    print(union)

if __name__ == "__main__":
    main()
