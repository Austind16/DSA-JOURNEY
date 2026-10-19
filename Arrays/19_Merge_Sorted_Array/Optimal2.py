# Problem: Merge Two Sorted Arrays Without Extra Space (Gap Method / Shell Sort)
# Time Complexity: O((N + M) * log(N + M)) — Logarithmic gap passes with linear swap scans.
# Space Complexity: O(1) auxiliary space — In-place array modification.
def merge_array(arr1: list[int], arr2: list[int]) -> list[int]:
    n = len(arr1)
    m = len(arr2)
    gap = ((m + n) // 2) + 1
    while gap > 0:
        left = 0
        right = left + gap
        while(right < m + n):
            if left < n and right >= n:
                swapifgreater(arr1, arr2, left, right - n)
            elif left >= n:
                swapifgreater(arr2, arr2, left - n, right - n)
            else:
                swapifgreater(arr1, arr1, left, right)

            left += 1
            right += 1
        if gap == 1:
            break
        else:
            gap = (gap // 2) + (gap % 2)

    return arr1, arr2

def swapifgreater(arr1, arr2, ind1, ind2):
    if arr1[ind1] > arr2[ind2]:
        arr1[ind1], arr2[ind2] = arr2[ind2], arr1[ind1]

def main():
    arr1 = [1, 3, 5, 7]
    arr2 = [0, 2, 6, 8, 9]
    merge_array(arr1, arr2)
    print(arr1, arr2)

if __name__ == "__main__":
    main()