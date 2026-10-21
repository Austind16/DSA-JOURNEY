def maximum_product(arr: list[int]) -> int:
    n = len(arr)
    max_prod = float('-inf')
    prefix = 1
    suffix = 1
    for i in range(n):
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1

        prefix *= arr[i]
        suffix *= arr[n- i - 1]
        max_prod = max(max_prod, max(prefix, suffix))

    return max_prod

def main():
    arr = [2, 3, -2, 4]
    ans = maximum_product(arr)
    print(ans)

if __name__ == "__main__":
    main()