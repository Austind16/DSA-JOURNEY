# Problem: Merge Overlapping Intervals (Optimal Single Pass Approach)
# Time Complexity: O(N log N) — Sorting takes O(N log N) + single linear pass takes O(N).
# Space Complexity: O(N) — Output list memory used to store merged intervals.
def merge_interval(arr: list[list]) -> list[list]:
    n = len(arr)
    ans = []
    arr.sort()

    for i in range(n):
        start = arr[i][0]
        end = arr[i][1]
        if len(ans) == 0 or start > ans[-1][1]:
            ans.append([start, end])
        else:
            ans[-1][1] = max(ans[-1][1], end)

    return ans

def main():
    arr = [[1,3],[2,6],[8,10],[15,18]]
    ans = merge_interval(arr)
    print(ans)

if __name__ == "__main__":
    main()