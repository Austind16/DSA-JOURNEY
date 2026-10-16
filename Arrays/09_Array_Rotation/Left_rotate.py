# Left Rotate Array by K Positions (Optimal Reversal Algorithm)
# Time Complexity: O(N) | Space Complexity: O(1)

def reverse(start: int, end: int, arr: list[int]) -> list[int]:
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


def left_rotate(k: int, arr: list[int]) -> list[int]:
    if not arr:
        return arr

    n = len(arr)
    k = k % n

    reverse(0, k - 1, arr)
    reverse(k, n - 1, arr)
    reverse(0, n - 1, arr)

    return arr


def main():
    arr = [1, 2, 3, 4, 5, 6, 7]

    k = int(input("Enter number of swap: "))

    solved_arr = left_rotate(k, arr)

    print(solved_arr)


if __name__ == "__main__":
    main()