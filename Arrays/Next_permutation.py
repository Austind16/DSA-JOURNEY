# Problem: Next Permutation (Optimal In-Place 3-Step Algorithm)
# Time Complexity: O(N) — Single-pass linear scans to find dip/swap target + single-pass array reversal.
# Space Complexity: O(1) — In-place array modification with constant extra space.
def next_permutation(arr: list[int]) -> list[int]:
    index = -1
    n = len(arr)
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            index = i
            break

    if index != -1:
        for i in range(n - 1, index, -1):
            if arr[i] > arr[index]:
                arr[i], arr[index] = arr[index], arr[i]
                break

    st = index + 1
    end = n - 1

    while st < end:
        arr[st], arr[end] = arr[end], arr[st]
        st += 1
        end -= 1

    return arr

def main():
    arr = [2, 1, 5, 4, 3, 0, 0]
    next_permutation(arr)
    print(arr)

if __name__ == "__main__":
    main()