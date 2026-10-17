# Problem: 4Sum (Brute Force Approach)
# Time Complexity: O(N^4) — Four nested loops generating all quadruplet combinations.
# Space Complexity: O(M) — Set memory storing unique quadruplets (M = count of unique quadruplets).
def foursum(target, arr: list[int]) -> list[list]:
    n = len(arr)
    ans = set()
    temp = []

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if arr[i] + arr[j] + arr[k] + arr[l] == target:
                        temp = [arr[i], arr[j], arr[k], arr[l]]
                        temp.sort()
                        ans.add(tuple(temp))

    return [list(quartets) for quartets in ans]

def main():
    arr = [1,0,-1,0,-2,2]
    target = 0
    ans = foursum(target, arr)
    print(ans)

if __name__ == "__main__":
    main()