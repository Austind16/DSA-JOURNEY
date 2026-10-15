# Problem: Set Matrix Zeroes (Brute Force Approach)
# Time Complexity: O((N * M) * (N + M)) — Scanning grid and marking row/col cells with -1.
# Space Complexity: O(1) — In-place modifications using temporary marker (-1).
def set_matrix_zeroes(arr: list[list]) -> list[list]:
    row = len(arr)
    col = len(arr[0])

    for i in range(row):
        for j in range(col):
            if arr[i][j] == 0:
                markrow(arr, col, i)
                markcol(arr, row, j)

    for i in range(row):
        for j in range(col):
            if arr[i][j] == -1:
                arr[i][j] = 0

    return arr 

def markrow(arr, col, i):
    for j in range(col):
        if arr[i][j] != 0:
            arr[i][j] = -1

def markcol(arr, row, j):
    for i in range(row):
        if arr[i][j] != 0:
            arr[i][j] = -1

def main():
    arr = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    set_matrix_zeroes(arr)
    print(arr)

if __name__ == "__main__":
    main()