def maximum_product(arr: list[int]) -> int:
    n = len(arr)
    max_prod = float('-inf')

    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod *= arr[j]
            max_prod = max(prod, max_prod)

    return max_prod

def main():
    arr = [2, 3, -2, 4]
    ans = maximum_product(arr)
    print(ans)

if __name__ == "__main__":
    main()