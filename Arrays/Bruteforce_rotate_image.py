# Problem: Rotate Image / Matrix 90 Degrees Clockwise (Brute Force Approach)
# Time Complexity: O(N^2) — Single pass over all N x N matrix elements.
# Space Complexity: O(N^2) — Uses an auxiliary matrix to store rotated positions.
def rotate(arr: list[list]) -> list[list]:
    row = len(arr)
    col = len(arr[0])
    ans = [[0] * row for _ in range(col)]

    ans_i = row
    for i in range(row):
        ans_i -= 1
        for j in range(col):
            ans[j][ans_i] = arr[i][j]

    return ans

def main():
    arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    ans = rotate(arr)
    print(ans)

if __name__ == "__main__":
    main()