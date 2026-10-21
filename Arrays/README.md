# 📚 Arrays

Welcome to the **Arrays** section of my DSA journey! This folder contains
Python implementations of popular array problems from platforms such as
LeetCode and GeeksforGeeks, with an emphasis on recognizing reusable patterns
and choosing optimal solutions.

The goal is to master array problem-solving fundamentals, understand
time/space trade-offs, and build the intuition needed to move from a brute
force solution to a clean, efficient implementation.

> **Complexity note:** Unless stated otherwise, space complexity refers to
> auxiliary space. Output storage may still require additional memory.

## 🧭 Master Problem Table

This is a curated quick-reference table for the currently documented
optimized solutions. It includes the eight problems listed below; the complete
folder navigation is available in the topic directory that follows.

| # | Problem Name | Platform / Equivalent | Core Pattern / Technique | Time Complexity | Space Complexity | File Link |
|---:|---|---|---|---:|---:|---|
| 1 | 3Sum Closest | LeetCode #16 | Sorting + Two Pointers | `O(N²)` | `O(1)` | [ThreeSum_II.py](./16_Three_Sum/ThreeSum_II.py) |
| 2 | 4Sum | LeetCode #18 | Sorting + Two Pointers | `O(N³)` | `O(1)` | [Optimal.py](./17_Four_sum/Optimal.py) |
| 3 | Count Subarrays with Given XOR K | GeeksforGeeks | Prefix XOR + Hash Map | `O(N)` | `O(N)` | [Optimal_subarray_XORk.py](./10_Subarrays_and_Sequences/Optimal_subarray_XORk.py) |
| 4 | Merge Overlapping Intervals | LeetCode #56 | Sorting + Single Pass | `O(N log N)` | `O(N)` | [Optimal.py](./18_Merge_Intervals/Optimal.py) |
| 5 | Merge Two Sorted Arrays Without Extra Space | GeeksforGeeks | Gap Method / Shell Sort | `O((N + M) log(N + M))` | `O(1)` | [Optimal2.py](./19_Merge_Sorted_Array/Optimal2.py) |
| 6 | Find Missing and Repeating Number | GeeksforGeeks | Mathematical Equations | `O(N)` | `O(1)` | [Optimal.py](./20_Missing_and_Repeating/Optimal.py) |
| 7 | Count Inversions | GeeksforGeeks | Merge Sort / Divide and Conquer | `O(N log N)` | `O(N)` | [Optimal.py](./21_Count_Inversions/Optimal.py) |
| 8 | Reverse Pairs | LeetCode #493 | Merge Sort + Two Pointers | `O(N log N)` | `O(N)` | [Optimal.py](./22_Reverse_pairs/Optimal.py) |

## 🧠 Key Array Patterns Covered

- **Two Pointers & Sliding Window**
  - Sort-and-scan techniques for 3Sum Closest and 4Sum.
  - Gap-based comparisons for merging sorted arrays in place.
  - Window-based reasoning for subarray and sequence problems.
- **Prefix Sums, Prefix XOR & Hash Maps**
  - Track running XOR values and their frequencies to count subarrays with
    a target XOR in linear time.
  - Use prefix-state lookups to replace repeated subarray calculations.
- **Sorting & Single-Pass Scans**
  - Sort intervals first, then merge overlapping ranges with one linear pass.
  - Use sorted order to simplify duplicate handling and pointer movement.
- **Divide and Conquer / Merge Sort**
  - Count inversions while merging sorted halves.
  - Count reverse pairs before merging, preserving `O(N log N)` performance.
- **Mathematical Tricks**
  - Use equations for sums and sums of squares to identify missing and
    repeating values with constant auxiliary space.
- **Complexity Optimization**
  - Compare brute-force, improved, and optimal approaches.
  - Balance runtime, auxiliary memory, readability, and in-place updates.

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Austind16/DSA-JOURNEY.git
cd DSA-JOURNEY/Arrays
```

### 2. Run any solution

Use the relative path to the solution file from the `Arrays/` directory:

```bash
python3 16_Three_Sum/ThreeSum_II.py
python3 21_Count_Inversions/Optimal.py
```

On Windows, `python` may be used instead:

```bash
python 22_Reverse_pairs/Optimal.py
```

Most scripts include a small `main()` function with sample input, making them
easy to execute and inspect independently.

## 🗂️ Topic Directory

| Folder | Focus |
|---|---|
| [`01_Searching`](./01_Searching) | Linear search |
| [`02_Array_Properties`](./02_Array_Properties) | Sorted arrays and consecutive ones |
| [`03_Sorting`](./03_Sorting) | Fundamental sorting algorithms |
| [`04_Two_Sum`](./04_Two_Sum) | Two Sum approaches |
| [`05_Union_and_Intersection`](./05_Union_and_Intersection) | Union and intersection |
| [`06_Largest_and_Second_Largest`](./06_Largest_and_Second_Largest) | Largest-element problems |
| [`07_Majority_Elements`](./07_Majority_Elements) | Majority-element problems |
| [`08_Missing_and_Appearing_Once`](./08_Missing_and_Appearing_Once) | Missing and single-occurrence values |
| [`09_Array_Rotation`](./09_Array_Rotation) | Array rotation |
| [`10_Subarrays_and_Sequences`](./10_Subarrays_and_Sequences) | Subarray and sequence problems |
| [`11_Array_Rearrangement`](./11_Array_Rearrangement) | Rearrangement and next permutation |
| [`12_Matrix_Problems`](./12_Matrix_Problems) | Matrix transformations |
| [`13_Array_Leaders`](./13_Array_Leaders) | Leaders in an array |
| [`14_Unique_Elements`](./14_Unique_Elements) | Unique-element approaches |
| [`15_Pascal's_Triangle`](./15_Pascal's_Triangle) | Pascal's Triangle |
| [`16_Three_Sum`](./16_Three_Sum) | 3Sum and 3Sum Closest |
| [`17_Four_sum`](./17_Four_sum) | 4Sum |
| [`18_Merge_Intervals`](./18_Merge_Intervals) | Merge overlapping intervals |
| [`19_Merge_Sorted_Array`](./19_Merge_Sorted_Array) | In-place merge of sorted arrays |
| [`20_Missing_and_Repeating`](./20_Missing_and_Repeating) | Missing and repeating values |
| [`21_Count_Inversions`](./21_Count_Inversions) | Inversion counting |
| [`22_Reverse_pairs`](./22_Reverse_pairs) | Reverse-pair counting |
| [`23_Maximum_Product_Array`](./23_Maximum_Product_Array) | Maximum product subarray |
| [`Stocks`](./Stocks) | Buy and sell stock |

---

⭐ Keep practicing, compare approaches, and turn every solved problem into a
reusable pattern!
