# Left Rotate Array by K Positions (Using Extra Space)
# Time Complexity: O(N) | Space Complexity: O(K)

def left_rotate_better(k: int, arr: list[int]) -> list[int]:
    if not arr:
        return arr

    n = len(arr)
    k = k % n

    temp = arr[:k]

    for i in range(0, n - k):
        arr[i] = arr[i + k]

    for i in range(0, len(temp)):
        arr[n - k + i] = temp[i]

    return arr


def main():
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = int(input("Enter shifting number: "))
    print(left_rotate_better(k, arr))


if __name__ == "__main__":
    main()