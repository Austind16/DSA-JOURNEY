# Problem: Maximum Subarray Sum (Optimal Kadane's Algorithm)
# Time Complexity: O(N) — Single linear scan through the array.
# Space Complexity: O(1) — Constant auxiliary space.
def maxsubarray(arr: list[int]) -> int:
    maxi = float('-inf')
    s = 0
    for i in range(len(arr)):
        s += arr[i]
        if s > maxi:
            maxi = s
        if s < 0:
            s = 0

    return maxi

def main():
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    num = maxsubarray(arr)
    print(num)

if __name__ == "__main__":
    main()