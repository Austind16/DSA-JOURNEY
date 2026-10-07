# Problem: Two Sum (Optimal Hash Map Approach)
# Time Complexity: O(N) — Single linear pass using O(1) hash map lookups.
# Space Complexity: O(N) — Storing elements and their indices in a dictionary.
def twosum(target, arr: list[int]) -> tuple[int, int] | None:
    seen = {}

    for i in range(len(arr)):
        num = arr[i]
        compliment = target - num

        if compliment in seen:
            return i, seen[compliment]

        seen[num] = i

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