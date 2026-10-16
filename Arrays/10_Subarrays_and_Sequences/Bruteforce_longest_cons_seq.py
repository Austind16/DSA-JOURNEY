# Problem: Longest Consecutive Sequence (Brute Force Approach)
# Time Complexity: O(N^3) — Linear lookup (num + 1 in arr) inside nested while and for loops.
# Space Complexity: O(1) — Constant auxiliary space.
def longest_cons_seq(arr: list[int]) -> int:
    mcount = 0
    for num in arr:
        count = 1
        while (num + 1) in arr:
           count += 1 
           num += 1
        if count > mcount:
            mcount = count

    return mcount

def main():
    arr = [102, 4, 100, 1, 101, 3, 2, 1, 1]
    mcount = longest_cons_seq(arr)
    print(mcount)

if __name__ == "__main__":
    main()