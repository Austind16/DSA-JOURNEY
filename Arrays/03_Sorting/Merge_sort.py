# Problem: Merge Sort (Divide & Conquer)
# Time Complexity: O(N log N) — Uniform across Best, Average, and Worst cases.
# Space Complexity: O(N) — Auxiliary space for the temporary merge buffer + O(log N) stack
def merge_sort(low, high, arr: list[int]) -> list[int]:
    if low >= high:
        return

    mid = (low + high) // 2
    merge_sort(low, mid, arr)
    merge_sort(mid + 1, high, arr)
    merge(low, mid, high, arr)

def merge(low, mid, high, arr: list[int]) -> list[int]:
    temp = []
    left = low
    right = mid + 1

    while (left <= mid and right <= high):
        if arr[left] < arr[right]:
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

def main():
    arr = [9, 4, 2, 6, 3, 5, 1, 7, 2]
    merge_sort(0, len(arr) - 1, arr)
    print(arr)

if __name__ == "__main__":
    main()