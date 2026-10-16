# Problem: Union of Two Sorted Arrays (Brute Force)
# Time Complexity: O((N+M) log(N+M)) | Space Complexity: O(N+M)
def sorted_array_union(arr1: list[int], arr2: list[int]) -> list[int]:
    unique_elements = set()

    for num in arr1:
        unique_elements.add(num)

    for num in arr2:
        unique_elements.add(num)

    union_list = sorted(list(unique_elements))
    
    return union_list

def main():
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr2 = [2, 3, 4, 4, 5, 11, 12]
    
    result = sorted_array_union(arr1, arr2)
    print("Union of arrays:", result)

if __name__ == "__main__":
    main()