# Problem: Reverse Pairs (Brute Force Approach)
# Time Complexity: O(N^2) — Two nested loops checking all unique pairs (i, j).
# Space Complexity: O(1) auxiliary space.
def reverse_pairs(arr: list[int]) -> int:
    n = len(arr)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > 2 * arr[j]:
                count += 1

    return count

def main():
    arr = [40, 25, 19, 12, 9, 6, 2]
    ans = reverse_pairs(arr)
    print(ans)

if __name__ == "__main__":
    main()