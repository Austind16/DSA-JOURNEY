# Problem: Selection Sort
# Time Complexity: O(N^2) — Best, Average, and Worst cases all require N(N-1)/2 comparisons.
# Space Complexity: O(1) — In-place sorting with constant auxiliary space.
def selection_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        mini = i
        for j in range (i + 1, len(arr)):
            if arr[j] < arr[mini]:
                mini = j
                
        if mini != i:
            arr[i], arr[mini] = arr[mini], arr[i]

    return arr

def main():
    arr = [6, 5, 2, 1, 3]
    ans = selection_sort(arr)
    print(ans)

if __name__ == "__main__":
    main()