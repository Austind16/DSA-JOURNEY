# Brute force second largest element search
# Time Complexity: O(N^2) | Space Complexity: O(1)
def brute_second_largest(arr: list[int]) -> int:
    n = len(arr)
    if n < 2:
        return -1
    
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
                
    largest = arr[-1]

    for i in range(n - 2, -1, -1):
        if arr[i] != largest:
            return arr[i]
            
    return -1

def main():
    arr = [1, 45, 54, 54, 4, 3, 2, 5, 6, 3, 26, 74]
    
    second_largest = brute_second_largest(arr)
    
    if second_largest != -1:
        print(f"Second largest element is {second_largest}")
    else:
        print("No second largest element found")


if __name__ == "__main__":
    main()