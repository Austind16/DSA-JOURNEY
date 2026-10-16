def majority(arr: list[int]) -> list[int]:
    n = len(arr)
    ans = []
    cnt1, cnt_1 = 0, 0
    cnt2, cnt_2 = 0, 0
    element1, element2 = None, None

    for num in arr:
        if(num == element1):
            cnt1 += 1
        
        elif(num == element2):
            cnt2 += 1

        elif cnt1 == 0:
            element1 = num
            cnt1 += 1

        elif cnt2 == 0:
            element2 = num
            cnt2 += 1

        else:
            cnt1 -= 1
            cnt2 -= 1

    for num in arr:
        if num == element1:
            cnt_1 += 1
        elif num == element2:
            cnt_2 += 1

    if cnt_1 > n // 3:
        ans.append(element1)
    if cnt_2 > n // 3:
        ans.append(element2)

    return ans

def main():
    arr = [1, 1, 1, 3, 3, 2, 2, 2]
    ans = majority(arr)
    print(ans)

if __name__ == "__main__":
    main()