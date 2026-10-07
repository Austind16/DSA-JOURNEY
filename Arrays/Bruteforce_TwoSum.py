# Problem: Two Sum (Brute Force Approach)
# Time Complexity: O(N^2) — Nested loops checking every possible pair.
# Space Complexity: O(1) — Constant auxiliary space.
def twosum(target, arr: list[int]) -> tuple[int, int] | None:
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return i, j

    return None

def main():
    arr = [1, 5, 6, 8, 4]
    target = 14
    result = twosum(target, arr)
    
    if result:
        i, j = result
        print(i,j)
    else:
        print("No two sum solution found.")

if __name__ == "__main__":
    main()