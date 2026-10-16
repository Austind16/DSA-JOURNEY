# Problem: Array Leaders (Optimal Right-to-Left Single-Pass Approach)
# Time Complexity: O(N) — Single backward linear scan tracking running maximum + O(N) list reversal.
# Space Complexity: O(1) auxiliary space (excluding space used for output list).
def leader(arr: list[int]) -> list[int]:
    n = len(arr)
    ans = []
    maxi = float('-inf')
    for i in range(n-1, -1, -1):
        if arr[i] >= maxi:
            maxi = arr[i]
            ans.append(arr[i])

    return ans[::-1]

def main():
    arr = [10, 22, 12, 3, 0, 6]
    ans = leader(arr)
    print(ans)

if __name__ == "__main__":
    main()