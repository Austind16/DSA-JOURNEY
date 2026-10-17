# Problem: 3Sum Closest (Optimal 2-Pointer Approach)
# Time Complexity: O(N^2) — Sorting takes O(N log N) + outer loop with 2-pointer scan takes O(N^2).
# Space Complexity: O(1) auxiliary space.
def Threesum(target, arr: list[int]) -> int:
    n = len(arr)
    dif = 0
    ans = 0
    closest = float('inf')

    arr.sort()

    for i in range(n):
        j = i + 1
        k = n - 1

        while j < k:
            total = arr[i] + arr[j] + arr[k]
            dif = abs(target - total)
            if dif < closest:
                closest = dif
                ans = total

            if total < target:
                j += 1

            elif total > target:
                k -= 1

            else:
                ans = target
                break

    return ans

def main():
    arr = [-1,2,1,-4]
    target = 1
    ans = Threesum(target, arr)
    print(ans)

if __name__ == "__main__":
    main()