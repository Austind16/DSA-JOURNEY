def majorityII(arr: list[int]) -> list[int]:
    hashi = {}
    ans = []

    mini = (len(arr) // 3) + 1
    for num in arr:
        hashi[num] = hashi.get(num, 0) + 1
        if hashi[num] == mini:
            ans.append(num)
        if len(ans) == 2:
            break

    return ans

def main():
    arr = [1, 1, 1, 3, 3, 2, 2, 2]
    ans = majorityII(arr)
    print(ans)

if __name__ == "__main__":
    main()