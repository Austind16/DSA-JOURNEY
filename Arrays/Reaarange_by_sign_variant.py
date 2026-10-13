# Problem: Rearrange Array Elements by Sign (Variety 2: Unequal Positive/Negative Counts)
# Time Complexity: O(N) — Linear scan to filter elements + linear scan to rebuild array.
# Space Complexity: O(N) — Auxiliary lists pos and neg to store elements before placing.
def rearrange(arr: list[int]) -> list[int]:
    n = len(arr)
    pos = []
    neg = []
    for num in arr:
        if num > 0:
            pos.append(num)
        if num < 0:
            neg.append(num)

    if len(pos) > len(neg):
        for i in range(0, len(neg)):
            arr[i * 2] = pos[i]
            arr[(i * 2) + 1] = neg[i]

        index = len(neg) * 2
        for i in range(len(neg), len(pos)):
            arr[index] = pos[i]
            index += 1

    elif len(neg) > len(pos):
        for i in range(0, len(pos)):
            arr[i * 2] = pos[i]
            arr[(i * 2) + 1] = neg[i]
        
        index = len(pos) * 2
        for i in range(len(pos), len(neg)):
            arr[index] = neg[i]
            index += 1

    else:
        for i in range(n // 2):
                arr[i * 2] = pos[i]
                arr[(i * 2) + 1] = neg[i]

    return arr

def main():
    arr = [-1, 2, 3, 4, -3, 1]
    rearrange(arr)
    print(arr)

if __name__ == "__main__":
    main()