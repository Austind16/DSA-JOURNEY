# Problem: Find the Number That Appears Once (Better / Hashing Approach)
# Time Complexity: O(N) — Single pass to populate hash array + single pass to check frequencies. Total: O(2N) = O(N).
# Space Complexity: O(max(arr)) — Auxiliary hash array allocated based on maximum element in array.
def check(arr: list[int]) -> int:
    maxi = max(arr) + 1
    hashi = [0] * maxi
    for num in arr:
        hashi[num] += 1

    for num in arr:
        if hashi[num] == 1:
            return num

def main():
    arr = [1, 1, 2, 3, 3, 4, 4]
    num = check(arr)
    print(num)

if __name__ == "__main__":
    main()