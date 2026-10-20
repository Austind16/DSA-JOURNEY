# Problem: Count Inversions in an Array (Optimal Merge Sort Approach)
# Time Complexity: O(N log N) — Divide and conquer tree traversal with linear merges.
# Space Complexity: O(N) — Auxiliary memory for temporary array merges.
cnt = 0
def divide(low, high, arr: list[int]) -> int:
    if low >= high:
        return

    mid = (low + high) //2
    divide(low, mid, arr)
    divide(mid + 1, high, arr)
    check(low, mid, high, arr)

def check(low, mid, high, arr):
    temp = []
    left = low
    right = mid + 1

    while (left <= mid and right <= high):
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            global cnt
            cnt += (mid - left + 1)
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
    arr = [5, 3, 2, 4, 1]
    n = len(arr)
    divide(0, n - 1, arr)
    print(cnt)

if __name__ == "__main__":
    main()