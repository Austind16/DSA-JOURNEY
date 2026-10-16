def subarray(k, arr: list[int]) -> int:
    n = len(arr)
    count = 0

    for i in range(n):
        sumi = 0
        for j in range(i, n):
            sumi += arr[j]
            if sumi == k:
                count += 1

    return count

def main():
    arr = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
    k = 3
    ans = subarray(k, arr)
    print(ans)

if __name__ == "__main__":
    main()