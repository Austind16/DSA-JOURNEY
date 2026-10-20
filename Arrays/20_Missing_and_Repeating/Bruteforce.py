# Problem: Find Missing and Repeating Number (Brute Force Approach)
# Time Complexity: O(N^2) — Two nested loops checking counts for each number from 1 to N.
# Space Complexity: O(1) auxiliary space.
def missing_repeating(arr: list[int]) -> int:
    n = len(arr)
    rep = -1
    miss = -1

    for i in range(1, n + 1):
        count = 0
        for j in range(n):
            if i == arr[j]:
                count += 1
        if count == 0:
            miss = i
        elif count == 2:
            rep = i

    return rep, miss

def main():
    arr = [4, 3, 6, 2, 1, 1]
    rep, miss = missing_repeating(arr)
    print(f"Missing number: {miss}") 
    print(f"Repeating number: {rep}") 

if __name__ == "__main__":
    main()