# Left Rotate Array by K Positions (Optimal Reversal Algorithm)
# Time Complexity: O(N) | Space Complexity: O(1)
def left_rotate(k, arr: list[int]) -> int:

    if not arr or len(arr) == 0:
        return


    k = k % len(arr)

    reverse(0, k-1, arr)
    reverse(k, len(arr) - 1, arr)
    reverse(0, len(arr) - 1, arr)

def reverse(start, end, arr: list[int]) -> int:
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]

        start += 1
        end -= 1


def main():
    arr = [1, 2, 3, 4, 5, 6, 7]

    k = int(input("Enter number of swap: "))

    left_rotate(k, arr)

    print(arr)

if __name__ == "__main__":
    main()