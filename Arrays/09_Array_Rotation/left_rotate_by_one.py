# Left Rotate Array by K Positions (Optimal Reversal Algorithm)
# Time Complexity: O(N) | Space Complexity: O(1)

def left_rotate_by_one(arr: list[int]) -> list[int]:

    if not arr or len(arr) == 1:
        return arr
    
    temp  = arr[0]
    n = len(arr)

    for i in range (1, n):
        arr[i - 1] = arr[i]

    arr[n - 1] = temp

    return arr

def main():
    arr = [1, 2, 3, 4, 5, 6, 7]

    left_rotate_by_one(arr)

    print(arr)

if __name__ == "__main__":
    main()