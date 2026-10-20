# Problem: Find Missing and Repeating Number (Better Hash/Frequency Array Approach)
# Time Complexity: O(N) — Two linear passes (frequency counting + evaluation loop).
# Space Complexity: O(N) — Auxiliary frequency array of size N + 1.
def missing_repeating(arr: list[int]) -> int:
    n = len(arr)
    miss = -1
    rep = -1
    ans = [0] * (n + 1)

    for i in range(n):
        ans[arr[i]] += 1

    for i in range(1, n + 1):
        if ans[i] == 0:
            miss = i
        elif ans[i] == 2:
            rep = i


    return rep, miss

def main():
    arr = [4, 3, 6, 2, 1, 1]
    rep, miss = missing_repeating(arr)
    print(f"Missing number: {miss}") 
    print(f"Repeating number: {rep}") 

if __name__ == "__main__":
    main()