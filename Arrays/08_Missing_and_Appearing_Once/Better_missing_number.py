# Problem: Find Missing Number in Array (Better / Hashing Approach)
# Time Complexity: O(N) — Single pass to populate hash frequency array + single pass to find missing element. Total: O(2N) = O(N).
# Space Complexity: O(N) — Auxiliary hash array of size N + 2 used to store element frequencies.
def hashing(arr: list[int]) -> int:
    n = len(arr)
    hash = [0] * (n+1)
    for num in arr:
        hash[num - 1] = 1
    for i in range(0, n + 1):
        if hash[i] == 0:
            return i + 1

def main():
    arr = [4, 3, 1, 2]
    num = hashing(arr)
    print(num)

if __name__ == "__main__":
    main()