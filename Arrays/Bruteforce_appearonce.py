# Problem: Find the Number That Appears Once (Brute Force Approach)
# Time Complexity: O(N^2) — Nested loops counting the frequency of each element in the array.
# Space Complexity: O(1) — No extra space used.
def check(arr: list[int]) -> int:
    for num1 in arr:
        count = 0 
        for num2 in arr:
            if num1 == num2:
                count += 1
        if count == 1:
            return num1

def main():
    arr = [1, 1, 2, 3, 3, 4, 4]
    num = check(arr)
    print(num)  # Outputs: 2

if __name__ == "__main__":
    main()