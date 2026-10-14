# Problem: Longest Consecutive Sequence (Better Sorting Approach)
# Time Complexity: O(N log N) — Sorting dominates the execution time.
# Space Complexity: O(1) or O(N) — Auxiliary space required by Timsort.
def longest_cons_seq(arr: list[int]) -> int:
    arr.sort()
    curr = 1
    last_small = float('-inf')
    longest = 1

    for num in arr:
        if last_small == (num - 1):
            curr += 1
            last_small = num
            if curr > longest:
                longest = curr
        elif last_small == num:
            continue
        else:
            last_small = num
            curr = 1

    return longest

def main():
    arr = [100, 102, 100, 101, 101, 4, 3, 2, 3, 2, 1, 1, 1, 2]
    longest = longest_cons_seq(arr)
    print(longest)

if __name__ == "__main__":
    main()