# Problem: Rotate Image / Matrix 90 Degrees Clockwise (Optimal In-Place Approach)
# Time Complexity: O(N^2) — O(N^2) for transposing the matrix + O(N^2) for reversing rows.
# Space Complexity: O(1) — In-place matrix rotation with no extra auxiliary matrix.
def rotate(arr: list[list]) -> list[list]:
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    for i in arr:
        reverse(i, 0, n - 1)
        
    return arr

def reverse(arr, st, end):
    while st < end:
        arr[st], arr[end] = arr[end], arr[st]
        st += 1
        end -= 1

def main():
    arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    rotate(arr)
    print(arr)

if __name__ == "__main__":
    main()