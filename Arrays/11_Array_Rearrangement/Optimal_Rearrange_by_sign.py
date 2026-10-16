# Problem: Rearrange Array Elements by Sign (Optimal 1-Pass 2-Pointer Approach)
# Time Complexity: O(N) — Single linear pass placing positive and negative numbers at target indices.
# Space Complexity: O(N) — Auxiliary array of size N to store rearranged result while maintaining relative order.
def rearrange(arr: list[int]) -> list[int]:
    n = len(arr)
    newarr = [0] * n
    i = 0
    j = 1
    for num in arr:
        if num > 0:
            newarr[i] = num
            i += 2
        elif num < 0:
            newarr[j] = num
            j += 2

    return newarr

def main():
    arr = [3, 1, -2, -5, 2, -4]
    ans = rearrange(arr)
    print(ans)

if __name__ == "__main__":
    main()