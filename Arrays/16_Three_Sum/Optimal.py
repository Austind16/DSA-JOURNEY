# Problem: 3Sum (Optimal 2-Pointer Approach)
# Time Complexity: O(N^2) — Sorting takes O(N log N) + outer loop with 2-pointer traversal takes O(N^2).
# Space Complexity: O(1) auxiliary space (excluding space used for the returned list).
def Threesum(arr: list[int]) -> list[list]:
    n = len(arr)
    ans = []
    arr.sort()

    for i in range(n):
        if(i >0 and arr[i] == arr[i - 1]):
            continue

        j = i + 1
        k = n - 1

        while j < k:
            total = arr[i] + arr[j] + arr[k]

            if total < 0:
                j += 1

            elif total > 0:
                k -= 1

            else:
                ans.append([arr[i], arr[j], arr[k]])

                j += 1
                k -= 1

                while j < k and arr[j] == arr[j - 1]:
                    j += 1
                while j < k and arr[k] == arr[k + 1]:
                    k -= 1

    return ans

def main():
    arr = [-1,0,1,2,-1,-4]
    ans = Threesum(arr)
    print(ans)

if __name__ == "__main__":
    main()