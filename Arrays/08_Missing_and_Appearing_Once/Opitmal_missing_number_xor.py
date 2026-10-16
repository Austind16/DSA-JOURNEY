# Problem: Find Missing Number in Array (Optimal Math Sum Approach)
# Time Complexity: O(N) — Single pass to calculate the sum of elements in the array.
# Space Complexity: O(1) — Constant extra space used for sum variables.
def xor(arr: list[int]) -> int:
    n = len(arr) + 1
    xor1 = 0
    xor2 = 0
    for i in range(0, n + 1):
        xor1 ^= i
    for num in arr:
        xor2 ^= num

    return xor1^xor2

def main():
    arr = [5, 3, 2, 1,]
    num = xor(arr)
    print(num)

if __name__ == "__main__":
    main()