# Brute Force Solution: Unique elements using a temporary collection
# Time Complexity: O(N) | Space Complexity: O(N)
def unique_element(arr: list[int]) -> int:
    
    unique_set = set()
    
    for num in arr:
        unique_set.add(num)

    unique_list = sorted(list(unique_set))

    k = len(unique_list)
    for i in range(k):
        arr[i] = unique_list[i]
        
    return k

def main():
    arr = [1, 1, 2, 2, 3, 3]

    k = unique_element(arr)

    print(k)
    print(arr)

if __name__ == "__main__":
    main()
