# Problem: Linear Search
# Time Complexity: O(N) | Space Complexity: O(1)
def linear_search(key, arr: list[int]) -> None:
    found_index = -1
    for i in range(0, len(arr)):
        if arr[i] == key:
            found_index = i
            break

    if found_index != -1:
        print(f"Element found at {found_index}")
    else:
        print("Element not found")

def main():
    arr = [1, 3, 4, 6, 8, 2, 0]
    key = int(input("Enter element to search: "))
    linear_search(key, arr)


if __name__ == "__main__":
    main()