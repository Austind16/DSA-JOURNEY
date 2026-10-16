# Problem: Array Leaders (Brute Force Approach)
# Time Complexity: O(N^2) — Nested loops comparing every element to all elements to its right.
# Space Complexity: O(1) auxiliary space (excluding space used for output list).
def leader(arr: list[int]) -> list[int]:
    n = len(arr)
    ans = []
    for i in range(0, n):
        flag = 0
        for j in range(i + 1, n):
            if arr[j] >= arr[i]:
                flag = 1
                break
        if flag != 1:
            ans.append(arr[i])

    return ans

def main():
    arr = [10, 22, 12, 3, 0, 6]
    ans = leader(arr)
    print(ans)

if __name__ == "__main__":
    main()