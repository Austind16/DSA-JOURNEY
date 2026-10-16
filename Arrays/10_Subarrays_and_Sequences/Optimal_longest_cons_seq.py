# Problem: Longest Consecutive Sequence (Optimal Hash Set Approach)
# Time Complexity: O(N) — O(N) to build set + O(N) linear traversal (each element visited at most twice).
# Space Complexity: O(N) — Auxiliary hash set to store distinct array elements for O(1) lookups.
def longest_cons_seq(arr: list[int]) -> int:
    sset = set(arr)
    longest = 1

    for num in sset:
        if (num - 1) not in sset:
            curr_num = num
            curr_cnt = 1

            while (curr_num + 1) in sset:
                curr_num += 1
                curr_cnt += 1

            longest = max(longest, curr_cnt)

    return longest

def main():
    arr = [100, 102, 100, 101, 101, 4, 3, 2, 3, 2, 1, 1, 1, 2]
    longest = longest_cons_seq(arr)
    print(longest)

if __name__ == "__main__":
    main()