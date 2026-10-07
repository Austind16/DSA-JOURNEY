def subarray(k, arr: list[int]) -> int:
    hashl = {0: -1}
    l = 0
    s = 0
    maxl = 0

    for i in range(len(arr)):
        s += arr[i]

        target = s - k
        if target in hashl:
            l = i - hashl[target]

            if l > maxl:
                maxl = l

        if s not in hashl:
                hashl[s] = i

    return maxl

def main():
    arr = [1, 1, 2, 3, 1, 1, 1, 3, 4, 2, 1]
    k = 3
    num = subarray(k, arr)
    print(num)

if __name__ == "__main__":
    main()