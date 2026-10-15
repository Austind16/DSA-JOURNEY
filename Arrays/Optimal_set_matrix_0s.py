# Problem: Set Matrix Zeroes (Optimal In-Place Approach)
# Time Complexity: O(N * M) — Constant linear passes over the N x M matrix.
# Space Complexity: O(1) — In-place tracking using matrix's 1st row & 1st col as markers.
def set_matrix_zeroes(arr: list[list]) -> list[list]:
    row = len(arr)
    col = len(arr[0])
    col0 = 1

    for i in range(row):
        for j in range(col):
            if arr[i][j] == 0:
                arr[i][0] = 0

                if j != 0:
                    arr[0][j] = 0
                else:
                    col0 = 0

    for i in range(1, row):
        for j in range(1, col):
            if arr[i][0] == 0 or arr[0][j] == 0:
                arr[i][j] = 0

    if arr[0][0] == 0:
        for j in range(col):
            arr[0][j] = 0

    if col0 == 0:
        for i in range(row):
            arr[i][0] = 0

    return arr

def main():
    arr = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    set_matrix_zeroes(arr)
    print(arr)

if __name__ == "__main__":
    main()