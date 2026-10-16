# Optimal solution second largest element search
# Time Complexity: O(N) | Space Complexity: O(1)
def optimal_second_largest_element(arr: list[int]) -> int:
    max_val = float('-inf')
    second_max = float('-inf')
    for num in arr:
        if num > max_val:
            second_max = max_val
            max_val = num
        elif num < max_val and num > second_max:
            second_max = num
    return second_max


# Optimal solution second smallest element search
# Time Complexity: O(N) | Space Complexity: O(1)
def optimal_second_smallest_element(arr: list[int]) -> int:
    min_val = arr[0]
    second_min = float('inf')
    for num in arr:
        if num < min_val:
            second_min = min_val
            min_val = num
        elif num != min_val and num < second_min:
            second_min = num
    return second_min


def main():
    arr = [1, 45, 54, 54, 4, 3, 2, 5, 6, 3, 26, 74]

    second_largest = optimal_second_largest_element(arr)
    second_smallest = optimal_second_smallest_element(arr)

    print(f"Second largest element is {second_largest}")
    print(f"Second smallest element is {second_smallest}")


if __name__ == "__main__":
    main()