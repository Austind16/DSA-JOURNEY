# Problem: Sort Colors / Sort an Array of 0s, 1s, and 2s (Better Counting Approach)
# Time Complexity: O(N) — Two-pass O(N) linear scan (Pass 1: Count frequencies, Pass 2: Overwrite array).
# Space Complexity: O(1) — Constant auxiliary space using integer counters.
def sort0_1_2(arr: list[int]) -> list[int]:
    count0 = 0
    count1 = 0
    count2 = 0
    for num in arr:
        if num == 0:
            count0 += 1
        elif num == 1:
            count1 += 1
        else:
            count2 += 1

    for i in range(0, count0):
        arr[i] = 0
    for i in range(count0, count0 + count1):
        arr[i] = 1
    for i in range(count0 + count1, len(arr)):
        arr[i] = 2

def main():
    arr = [0, 2, 2, 1, 0, 0, 1, 1, 2]
    sort0_1_2(arr)
    print(arr)

if __name__ == "__main__":
    main()