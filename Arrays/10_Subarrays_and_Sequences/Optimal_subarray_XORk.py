def subarray_XOR(k, arr: list[int]) -> int:
    n = len(arr)
    hashi = {0: 1}
    ans = 0
    xor_sum = 0
    for i in range(n):
        xor_sum = xor_sum ^ arr[i]
        target  = xor_sum ^ k

        if target in hashi:
            ans += hashi[target]

        hashi[xor_sum] = hashi.get(xor_sum, 0) + 1

    return ans

def main():
    arr = [4, 2, 2, 6, 4]
    k = 6
    ans, hashi = subarray_XOR(k, arr)
    print(ans)

if __name__ == "__main__":
    main()