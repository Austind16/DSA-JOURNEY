# Problem: Count Inversions in an Array (Brute Force Approach)
# Time Complexity: O(N^2) — Two nested loops iterating over all unique index pairs (i, j).
# Space Complexity: O(1) auxiliary space.
def count_inversions(arr: list[int]) -> int:
    n = len(arr)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1

    return count

def main():
    arr = [5, 3, 2, 4, 1]
    ans = count_inversions(arr)
    print(ans)

if __name__ == "__main__":
    main()