# Problem: Majority Element II (Brute Force Approach)
# Time Complexity: O(N^2) — Nested linear scans to count frequencies of unique elements.
# Space Complexity: O(1) auxiliary space (output list stores at most 2 elements).
def majorityII(arr: list[int]) -> list[int]:
    n = len(arr)
    ans = []

    for i in range(n):
        if arr[i] not in ans:
            count = 0
            for j in range(n):
                if arr[i] == arr[j]:
                    count += 1

            if count > n // 3:
                ans.append(arr[i]) 

        if len(ans) == 2:
            break

    return ans

def main():
    arr = [1, 1, 1, 3, 3, 2, 2, 2]
    ans = majorityII(arr)
    print(ans)

if __name__ == "__main__":
    main()