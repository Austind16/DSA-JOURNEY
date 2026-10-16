# Optimal solution: Remove duplicates in-place from a sorted array
# Time Complexity: O(N) | Space Complexity: O(1)
def unique_element(arr: list[int]) -> int:
    if not arr:
        return 0

    i = 0

    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]

    return i + 1

def main():
    arr = [1, 1, 2, 2, 3, 3]

    k = unique_element(arr)

    print(k)
    print(arr)

if __name__ == "__main__":
    main()
