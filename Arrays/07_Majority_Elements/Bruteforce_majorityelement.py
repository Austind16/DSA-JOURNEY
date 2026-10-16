# Problem: Majority Element (> N/2 times) (Brute Force Approach)
# Time Complexity: O(N^2) — Nested loops counting frequency of every element.
# Space Complexity: O(1) — Constant auxiliary space.
def majority(arr: list[int]) -> int:
    n = len(arr)
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
        if count > n//2:
            return arr[i]

def main():
    arr = [1, 2, 2, 3, 2, 2, 5]
    num = majority(arr)
    print(num)

if __name__ == "__main__":
    main()