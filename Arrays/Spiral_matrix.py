# Problem: Spiral Matrix (Optimal 4-Pointer Boundary Approach)
# Time Complexity: O(N * M) — Visits every element in the N x M matrix exactly once.
# Space Complexity: O(1) auxiliary space (excluding space used for the output list).
def spiral_matrix(arr: list[int]) -> list[int]:
    n = len(arr)
    m = len(arr[0])
    ans = []
    top = 0
    left = 0
    right = m - 1
    bottom = n - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            ans.append(arr[top][i])
        top += 1

        for i in range(top, bottom + 1):
            ans.append(arr[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                ans.append(arr[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                ans.append(arr[i][left])
            left += 1

    return ans 

def main():
    arr = [
    [1, 2, 3, 4, 5, 6],
    [20, 21, 22, 23, 24, 7],
    [19, 32, 33, 34, 25, 8],
    [18, 31, 36, 35, 26, 9],
    [17, 30, 29, 28, 27, 10],
    [16, 15, 14, 13, 12, 11]
    ]
    ans = spiral_matrix(arr)
    print(ans)

if __name__ == "__main__":
    main()