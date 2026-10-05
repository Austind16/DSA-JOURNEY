# Problem: Find the Number That Appears Once (Better Hash Map / Dictionary Approach)
# Time Complexity: O(N) — Single pass to build frequency map + single pass over unique dictionary keys.
# Space Complexity: O(N) — Auxiliary hash map storing at most (N / 2) + 1 unique elements.
def check_dict(arr: list[int]) -> int:
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    for num, count in freq.items():
        if count == 1:
            return num

    return -1


def main():
    arr = [4, 1, 2, 1, 2]
    num = check_dict(arr)
    print("Single Element:", num)  # Output: 4


if __name__ == "__main__":
    main()