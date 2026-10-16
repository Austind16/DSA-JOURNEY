# Problem: Majority Element (> N/2 times) (Better Hash Map / Frequency Count Approach)
# Time Complexity: O(N) — Linear pass to populate map + linear pass to locate majority element.
# Space Complexity: O(N) — Auxiliary hash map storing element frequencies.
def majority(arr: list[int]) -> int:
    n = len(arr)
    hashi = {}
    for num in arr:
        if num in hashi:
            hashi[num] = hashi.get(num, 0) + 1

    for num, count in hashi.items():
        if count > n // 2:
            return num

def main():
    arr = [1, 2, 2, 3, 2, 2, 5]
    num = majority(arr)
    print(num)

if __name__ == "__main__":
    main()