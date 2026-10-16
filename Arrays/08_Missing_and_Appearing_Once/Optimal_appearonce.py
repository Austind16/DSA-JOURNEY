# Problem: Find the Number That Appears Once (Optimal Bitwise XOR Approach)
# Time Complexity: O(N) — Single pass through the array.
# Space Complexity: O(1) — Uses constant auxiliary space.

def single_number_optimal(arr: list[int]) -> int:
    xor_sum = 0
    
    # XOR all elements together; duplicates cancel out
    for num in arr:
        xor_sum ^= num
        
    return xor_sum


def main():
    arr = [4, 1, 2, 1, 2]
    num = single_number_optimal(arr)
    print("Single Element:", num)  # Output: 4


if __name__ == "__main__":
    main()