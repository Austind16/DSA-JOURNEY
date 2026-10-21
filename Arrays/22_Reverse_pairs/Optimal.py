# Problem: Reverse Pairs (Optimal Merge Sort Approach)
# Time Complexity: O(N log N) — Divide & conquer traversal with O(N) counting and merging per level.
# Space Complexity: O(N) — Auxiliary memory for temporary array merges.
def count_pairs(arr: list[int], low: int, mid: int, high: int) -> int:
    cnt = 0
    right = mid + 1

    for i in range(low, mid + 1):
        while right <= high and arr[i] > 2 * arr[right]:
            right += 1
        cnt += (right - (mid + 1))

    return cnt


def merge(arr: list[int], low: int, mid: int, high: int) -> None:
    temp = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(len(temp)):
        arr[low + i] = temp[i]


def reverse_pairs(low: int, high: int, arr: list[int]) -> int:
    if low >= high:
        return 0

    mid = (low + high) // 2
    cnt = reverse_pairs(low, mid, arr)
    cnt += reverse_pairs(mid + 1, high, arr)

    cnt += count_pairs(arr, low, mid, high)
    merge(arr, low, mid, high)

    return cnt


def main():
    arr = [40, 25, 19, 12, 9, 6, 2]
    n = len(arr)
    ans = reverse_pairs(0, n - 1, arr)
    print("Total Reverse Pairs:", ans)


if __name__ == "__main__":
    main()