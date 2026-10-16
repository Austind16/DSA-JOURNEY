# Problem: Two Sum (Sorting + Two-Pointer Approach)
# Time Complexity: O(N log N) — Sorting the array of (value, index) tuples dominates the execution time.
# Space Complexity: O(N) — Auxiliary space used to store original indices alongside array values.
def twosum(target, arr: list[int]) -> tuple[int, int] | None:
    indexed_arr = []
    for idx in range(len(arr)):
        indexed_arr.append((arr[idx], idx))

    indexed_arr.sort()
    
    i, j = 0, len(indexed_arr) - 1
    while i < j:
        current_sum = indexed_arr[i][0] + indexed_arr[j][0]
        
        if current_sum == target:
            return indexed_arr[i][1], indexed_arr[j][1]
        
        if current_sum < target:
            i += 1
        else:
            j -= 1
            
    return None

def main():
    arr = [1, 5, 6, 8, 4]
    target = 14
    result = twosum(target, arr)
    
    if result:
        i, j = result
        print(i, j)
    else:
        print("No two sum solution found.")

if __name__ == "__main__":
    main()