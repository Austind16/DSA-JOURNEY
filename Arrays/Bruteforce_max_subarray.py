# Problem: Maximum Subarray Sum (Brute Force Approach)
# Time Complexity: O(N^2) — Nested loops calculating all contiguous subarray sums.
# Space Complexity: O(1) — Uses constant auxiliary space
def maxsubarray(arr: list[int]) -> int:
    n = len(arr)
    maxi = float('-inf')
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += arr[j]
            if s > maxi:
                maxi = s

    return maxi

def main():
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    num = maxsubarray(arr)
    print(num)

if __name__ == "__main__":
    main()