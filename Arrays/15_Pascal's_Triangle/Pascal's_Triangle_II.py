def Pascal_II(n, arr: list[int]) -> list[int]:
    temp = 1

    for i in range(1, n):
        temp *= n - i
        temp //= i
        arr.append(temp)

    return arr

def main():
    arr = [1]
    n = 4
    Pascal_II(n, arr)
    print(arr)

if __name__ == "__main__":
    main()