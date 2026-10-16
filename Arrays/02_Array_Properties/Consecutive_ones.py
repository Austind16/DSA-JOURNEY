# Problem: Max Consecutive Ones
# Time Complexity: O(N) — Single linear pass through the array.
# Space Complexity: O(1) — Uses constant extra space for counter variables.
def consecutive_ones(arr: list[int]) -> int:
    count, maximum = 0, 0
    for num in arr:
        if num == 1:
            count += 1
        else:
            count = 0
        if maximum < count:
            maximum = count

    return maximum

def main():
    arr = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1]
    num = consecutive_ones(arr)
    print(num)

if __name__ == "__main__":
    main()