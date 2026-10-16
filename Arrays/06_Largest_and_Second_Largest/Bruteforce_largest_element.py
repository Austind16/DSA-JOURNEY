# Brute force: Sort the array in ascending order then take last element
# Time Complexity: O(N^2) | Space Complexity: O(1)
def brute_largest_element(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def main():
    arr = [1, 45, 54, 54, 4, 3, 2, 5, 6, 3, 26, 74]
    
    brute_largest_element(arr)
    
    print("Sorted Array:", arr)
    print(f"Largest element is {arr[-1]}")


if __name__ == "__main__":
    main()