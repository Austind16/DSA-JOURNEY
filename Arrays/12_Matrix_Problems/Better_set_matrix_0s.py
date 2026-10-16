# Problem: Set Matrix Zeroes (Better Dummy Array Approach)
# Time Complexity: O(N * M) — Two linear passes over the N x M matrix.
# Space Complexity: O(N + M) — Extra memory for row_mat and col_mat tracking arrays.
def set_matrix_zeroes(arr: list[list]) -> list[list]:
    row = len(arr)
    col = len(arr[0])
    row_mat = [0] * row
    col_mat = [0] * col

    for i in range(row):
        for j in range(col):
            if arr[i][j] == 0:
                row_mat[i] = 1
                col_mat[j] = 1

    for i in range(row):
        for j in range(col):
            if row_mat[i] == 1 or col_mat[j] == 1:
                arr[i][j] = 0

    return arr

def main():
    arr = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    set_matrix_zeroes(arr)
    print(arr)

if __name__ == "__main__":
    main()