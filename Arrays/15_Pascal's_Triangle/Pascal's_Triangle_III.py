# Problem: Pascal's Triangle (Generate First N Rows)
# Time Complexity: O(N^2) — Single pass generating N rows using ratio multiplication.
# Space Complexity: O(1) auxiliary space (excluding output 2D list).
def Pascal_III(n, arr: list[list[int]]) -> list[list[int]]:

    for j in range(1, n + 1):
        temp = 1
        temp_arr = [1]
        for i in range(1, j):
            temp *= j - i
            temp //= i
            temp_arr.append(temp)
        arr.append(temp_arr)

    return arr

def main():
    arr = []
    n = 7
    Pascal_III(n, arr)
    print(arr)

if __name__ == "__main__":
    main()