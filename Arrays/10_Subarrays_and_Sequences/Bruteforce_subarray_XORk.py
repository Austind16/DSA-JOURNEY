# Problem: Count Subarrays with Given XOR K (Brute Force Approach)
# Time Complexity: O(N^2) — Two nested loops calculating running XOR sums.
# Space Complexity: O(1) auxiliary space.
def subarray_XOR(k, arr: list[int]) -> int:
    n = len(arr)
    ans = 0
    for i in range(n):
        xor_sum = 0
        for j in range(i , n):
            xor_sum = xor_sum ^ arr[j]
            if xor_sum == k:
                ans += 1

    return ans

def main():
    arr = [4, 2, 2, 6, 4]
    k = 6
    ans = subarray_XOR(k, arr)
    print(ans)

if __name__ == "__main__":
    main()