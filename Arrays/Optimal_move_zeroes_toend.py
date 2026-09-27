# Problem: Move Zeroes to End (Optimal In-Place Solution)
# Time Complexity: O(N)
# Space Complexity: O(1)
def zeroes_to_end(arr: list[int]) -> list[int]:
    n = len(arr)
    i = 0

    for j in range(0, n):
        if(arr[j] != 0):
            arr[i] = arr[j]
            i += 1

    for j in range(i, n):
        arr[j] = 0

    return arr

def main():
    arr = [1, 0, 5, 0, 3, 0, 0, 2, 5, 1]
    new_arr = zeroes_to_end(arr)
    print(new_arr)

if __name__ == "__main__":
    main()