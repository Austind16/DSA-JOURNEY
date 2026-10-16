# Problem: Rearrange Array Elements by Sign
# Time Complexity: O(N) — Single linear scan placing positive and negative elements at target indices.
# Space Complexity: O(N) — Auxiliary array of size N required to preserve relative ordering.
def rearrange(arr: list[int]) -> list[int]:
    n = len(arr)
    pos = []
    neg = []
    for num in arr:
        if num > 0:
            pos.append(num)
        if num < 0:
            neg.append(num)

    for i in range(n // 2):
        arr[i * 2] = pos[i]
        arr[(i * 2) + 1] = neg[i]

    return arr

def main():
    arr = [3, 1, -2, -5, 2, -4]
    rearrange(arr)
    print(arr)

if __name__ == "__main__":
    main()