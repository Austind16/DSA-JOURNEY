# Optimal solution: Largest element search
# Time Complexity: O(N) | Space Complexity: O(1)
def optimal_largest_element(arr: list[int]) -> int:
    max_val = float('-inf')
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val


def main():
    arr = [1, 45, 54, 54, 4, 3, 2, 5, 6, 3, 26, 74]

    largest = optimal_largest_element(arr)

    print(f"Largest element is {largest}")


if __name__ == "__main__":
    main()