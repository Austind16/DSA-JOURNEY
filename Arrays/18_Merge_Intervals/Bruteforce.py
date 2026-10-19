# Problem: Merge Overlapping Intervals (Brute Force Approach)
# Time Complexity: O(N log N) — Sorting takes O(N log N) + outer/inner loops take O(2N).
# Space Complexity: O(N) — Output list memory used to store merged intervals.
def merge_interval(arr: list[list]) -> list[list]:
    n = len(arr)
    ans = []
    arr.sort()

    for i in range(n):
        start = arr[i][0]
        end = arr[i][1]
        if len(ans) != 0 and start <= ans[-1][1]:
            continue

        for j in range(i + 1, n):
            if arr[j][0] <= end:
                end = max(end, arr[j][1])
            else:
                break
        ans.append([start, end])

    return ans

def main():
    arr = [[1,3],[2,6],[8,10],[15,18]]
    ans = merge_interval(arr)
    print(ans)

if __name__ == "__main__":
    main()