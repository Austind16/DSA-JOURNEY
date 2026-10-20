# Problem: Find Missing and Repeating Number (Optimal Math Approach)
# Time Complexity: O(N) — Single linear pass to calculate array sums and square sums.
# Space Complexity: O(1) auxiliary space — Pure mathematical evaluation.
def missing_repeating(arr: list[int]) -> int:
    n = len(arr)
    miss, rep = -1, -1
    s = (n * (n  + 1)) // 2
    sn = (n * (n + 1) * (2 * n + 1)) // 6
    s2, sn2 = 0, 0

    for i in range(n):
        s2 += arr[i]
        sn2 += (arr[i]) ** 2

    val1 = s2 - s
    val2 = sn2 - sn
    val2 = val2 // val1
    rep = (val1 + val2) // 2
    miss = val2 - rep

    return rep, miss    

def main():
    arr = [4, 3, 6, 2, 1, 1]
    rep, miss = missing_repeating(arr)
    print(f"Missing number: {miss}") 
    print(f"Repeating number: {rep}") 

if __name__ == "__main__":
    main()