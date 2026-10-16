def subarray(k, arr: list[int]) -> int:
    hashi = {0: 1}
    sumi = 0
    count = 0

    for i in range(len(arr)):
        sumi += arr[i]
        target = sumi - k

        if target in hashi:
            count += hashi[target]

        if sumi in hashi:
            hashi[sumi] += 1

        else:
            hashi[sumi] = 1

    return count

def main():
    arr = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
    k = 3
    ans= subarray(k, arr)
    print(ans)

if __name__ == "__main__":
    main()