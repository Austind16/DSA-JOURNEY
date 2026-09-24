# Better Solution: Second largest element search (Two Passes)
# Time Complexity: O(2N) = O(N) | Space Complexity: O(1)
def better_second_largest(arr: list[int]) -> int:
    if len(arr) < 2:
        return -1

    largest = float('-inf')
    for num in arr:
        if num > largest:
            largest = num

    second_largest = float('-inf')
    for num in arr:
        if num > second_largest and num != largest:
            second_largest = num

    return second_largest if second_largest != float('-inf') else -1


def main():
    arr = [1, 45, 54, 54, 4, 3, 2, 5, 6, 3, 26, 74]

    smax = better_second_largest(arr)

    if smax == -1:
        print("No second largest element exists")
    else:
        print(f"Second largest element is {smax}")


if __name__ == "__main__":
    main()