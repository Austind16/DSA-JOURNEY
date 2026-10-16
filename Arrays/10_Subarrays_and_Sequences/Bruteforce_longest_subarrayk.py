# Problem: Longest Subarray with Sum K (Brute Force Approach)
# Time Complexity: O(N^2) — Nested loops checking all contiguous subarray sums.
# Space Complexity: O(1) — Uses constant extra space.
def subarray(k, arr: list[int]) -> int:
    n = len(arr)
    l = 0
    max_l = 0
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += arr[j]
            if s == k:
                l = j - i + 1
                if max_l < l:
                    max_l = l

    return max_l

def main():
    arr = [1, 1, 2, 3, 1, 1, 1, 3, 4, 2, 1]
    k = 3
    num = subarray(k, arr)
    print(num)

if __name__ == "__main__":
    main()