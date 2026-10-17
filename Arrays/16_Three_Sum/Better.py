# Problem: 3Sum (Better Hash Set Approach)
# Time Complexity: O(N^2) — Two nested loops with O(1) hash set lookups for the 3rd element.
# Space Complexity: O(N + M) — O(N) space for hash set + O(M) space for unique triplets set.
def Threesum(arr: list[int]) -> list[list]:
    n = len(arr)
    ans = set()
    temp = ()

    for i in range(n):
        hashi = set()
        for j in range(i + 1, n):
            third = -(arr[i] + arr[j])
            if third in hashi:
                temp = [arr[i], arr[j], third]
                temp.sort()
                ans.add(tuple(temp))
            hashi.add(arr[j])

    return[list(triplet) for triplet in ans]

def main():
    arr = [-1,0,1,2,-1,-4]
    ans = Threesum(arr)
    print(ans)

if __name__ == "__main__":
    main()