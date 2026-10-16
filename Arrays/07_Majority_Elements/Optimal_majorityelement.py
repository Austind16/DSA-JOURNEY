# Problem: Majority Element (> N/2 times) (Optimal Boyer-Moore Voting Algorithm)
# Time Complexity: O(N) — Single pass to find candidate + single pass to verify frequency.
# Space Complexity: O(1) — Constant auxiliary space (No hash map required).
def majority(arr: list[int]) -> int:
    n = len(arr)
    count = 0
    count1= 0
    for i in range(n):
        if count == 0:
            element = arr[i]
            count  = 1
        elif arr[i] == element:
            count += 1
        else:
            count -= 1

    for i in range(n):
        if arr[i] == element:
            count1 += 1
            if count1 > n // 2:
                return arr[i]

def main():
    arr = [1, 2, 2, 3, 2, 2, 5]
    num = majority(arr)
    print(num)

if __name__ == "__main__":
    main()