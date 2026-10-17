# Problem: 3Sum (Brute Force Approach)
# Time Complexity: O(N^3) — Three nested loops iterating through all triplet combinations.
# Space Complexity: O(M) — Set memory to store unique triplets (M = number of unique triplets).
def Threesum(arr: list[int]) -> list[list]:
    n = len(arr)
    ans = set()
    temp = ()

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    temp = [arr[i], arr[j], arr[k]]
                    temp.sort()
                    ans.add(tuple(temp))

    return [list(triplet) for triplet in ans]

def main():
    arr = [-1,0,1,2,-1,-4]
    ans = Threesum(arr)
    print(ans)

if __name__ == "__main__":
    main()