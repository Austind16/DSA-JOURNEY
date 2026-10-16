# Check whether the array is sorted in ascending order 
# Time Complexity: O(N) | Space Complexity: O(1) 

def check_sorted(arr: list[int]) -> bool:
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def main():
    arr = [1, 45, 54, 54, 4, 3, 2, 5, 6, 3, 26, 74]

    if check_sorted(arr):
        print("Array is sorted")
    else:
        print("Array is not sorted")

if __name__ == "__main__":
    main()
