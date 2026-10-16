# Problem: Move Zeroes to End (Brute Force / Auxiliary Space Approach)
# Time Complexity: O(N) | Space Complexity: O(N)
def zeroes_to_end(arr: list[int]) -> list[int]:

    n = len(arr)
    temp = []
    for i in range(0, n):
        if(arr[i] != 0):
            temp.append(arr[i])

    for i in range(0, len(temp)):
        arr[i] = temp[i]

    for i in range(len(temp), n):
        arr[i] = 0

    return arr

def main():
    arr = [1, 0, 5, 0, 3, 0, 0, 2, 5, 1]
    print(arr)

if __name__ == "__main__":
    main()