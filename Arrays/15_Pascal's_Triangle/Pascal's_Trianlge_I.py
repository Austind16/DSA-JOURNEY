# Problem: Pascal's Triangle - Variation 1 (Find Element at Row N, Column R)
# Time Complexity: O(R) — Single loop running R times to compute (N-1) C (R-1).
# Space Complexity: O(1) — Constant auxiliary space.
def Pascal_I(n, r):
    res = 1
    for i in range(r):
        res = (res * (n - i)) // (i + 1)

    return res

def main():
    n = 5
    r = 3
    ans = Pascal_I(n - 1, r - 1)
    print(ans)

if __name__ == "__main__":
    main()