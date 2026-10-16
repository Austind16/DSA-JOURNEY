# Problem: Intersection of Two Arrays (Brute Force Approach)
# Time Complexity: O(N1 * N2) — Nested loops checking every pair of elements.
# Space Complexity: O(N2) — Extra visited array to keep track of matched elements in arr2.
def intersection(arr1: list[int], arr2: list[int]) -> list[int]:

    inter = []
    visited = [False] * len(arr2)

    for i in range(0, len(arr1)):
        for j in range(0, len(arr2)):
            if (arr1[i] == arr2[j] and visited[j] == False):
                inter.append(arr1[i])
                visited[j] = True
                break

    return inter


def main():
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr2 = [2, 3, 4, 4, 5, 11, 12]

    res = intersection(arr1, arr2)
    print(res)

if __name__ == "__main__":
    main()