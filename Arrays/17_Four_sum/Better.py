# Problem: 4Sum (Better Hash Set Approach)
# Time Complexity: O(N^3) — Three nested loops with O(1) hash set lookups for the 4th element.
# Space Complexity: O(N + M) — O(N) auxiliary space for hash set + O(M) space for output set.
def foursum(target, arr: list[int]) -> list[list]:
    n = len(arr)
    ans = set()
    temp = []

    for i in range(n):
        for j in range(i + 1, n):
            hashi = set()
            for k in range(j + 1, n):
                fourth = target - (arr[i] + arr[j] + arr[k])
                if fourth in hashi:
                    temp = [arr[i], arr[j], arr[k], fourth]
                    temp.sort()
                    ans.add(tuple(temp))
                hashi.add(arr[k])

    return[list(quartet) for quartet in ans]

def main():
    arr = [1,0,-1,0,-2,2]
    target = 0
    ans = foursum(target, arr)
    print(ans)

if __name__ == "__main__":
    main()