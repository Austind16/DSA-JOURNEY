# Problem: Longest Subarray with Sum K (Optimal Two-Pointer / Sliding Window Approach)
# Time Complexity: O(N) — Both pointers i and j traverse the array at most once.
# Space Complexity: O(1) — Constant auxiliary space (No hash map used).
def subarray(k, arr: list[int]) -> int:
    i = 0
    s = 0
    l = 0
    maxl = 0
    for j in range(len(arr)):
        s += arr[j]

        while s >  k and i <= j:
            s -= arr[i]
            i += 1

        if s == k:
            l = j - i + 1
            if l > maxl:
                maxl = l

    return maxl

def main():
    arr = [1, 1, 2, 3, 1, 1, 1, 3, 4, 2, 1]
    k = 3
    num = subarray(k, arr)
    print(num)

if __name__ == "__main__":
    main()