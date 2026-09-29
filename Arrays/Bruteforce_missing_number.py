# Problem: Find Missing Number in Array (Brute Force Approach)
# Time Complexity: O(N^2) — Nested loop checking presence of each number from 1 to N in the array.
# Space Complexity: O(1) — No extra space used.
def missing(arr: list[int]) -> int:

    n = len(arr) + 1
    flag = 0

    for i in range(1, n + 1):
        for num in arr:
            if i == num:
                flag = 1
                break
        else:
            return i 

def main():
    arr = [5, 4, 1, 2]
    num = missing(arr)
    print(num)

if __name__ == "__main__":
    main()