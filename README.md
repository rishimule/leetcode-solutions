# LeetCode Solutions

Welcome to my LeetCode solutions repository! This repository contains my solutions to various LeetCode problems, categorized by difficulty and topic. The solutions are implemented in multiple programming languages, including Python, Java, and SQL

## Table of Contents

- [Getting Started](#getting-started)
- [Problem Categories](#problem-categories)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

To get started with the solutions, simply clone this repository to your local machine:

```bash
git clone https://github.com/rishimule/leetcode-solutions.git
```

## Solution Format

Each solution is organized in a separate file named after the problem title, following this format:

```
<Problem_Title>.<language_extension>
```

### Example Structure
```
/2191-sort-the-jumbled-numbers
  ├── 2191-sort-the-jumbled-numbers.py  <!-- Example solution file for Sort the Jumbled Numbers problem in Python -->
  ├── README.md  <!-- Problem Description -->
```

## Example Problem

### Problem: Sort the Jumbled Numbers problem in Python
- **Link**: [Sort the Jumbled Numbers problem in Python](https://leetcode.com/problems/sort-the-jumbled-numbers/)  <!-- Link to the problem -->
- **Description**: You are given a 0-indexed integer array mapping which represents the mapping rule of a shuffled decimal system. mapping[i] = j means digit i should be mapped to digit j in this system. The mapped value of an integer is the new integer obtained by replacing each occurrence of digit i in the integer with mapping[i] for all 0 <= i <= 9. You are also given another integer array nums. Return the array nums sorted in non-decreasing order based on the mapped values of its elements. <!-- Description of the problem -->

#### Solution (Python)
```python
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def translate_integer(num: int) -> int:
            digits: list[str] = list(str(num))
            for i in range(len(digits)):
                digits[i] = str(mapping[int(digits[i])])
            return int("".join(digits))

        number_mapping: dict[int, int] = {}
        for num in nums:
            number_mapping[num] = translate_integer(num)
        nums.sort(key=lambda val: number_mapping[val])

        return nums
```

#### Usage
```python
mapping = [8,9,4,0,2,1,3,5,7,6]
nums = [991,338,38]

s = Solution()
output = s.sortJumbled(mapping, nums)

print(output)  # Output: [338, 38, 991]  <!-- Expected output -->
```

## Contributing

Contributions are welcome! If you have solved a problem that is not yet included in this repository, please feel free to submit a pull request with your solution.  <!-- Invitation for others to contribute -->

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.  <!-- Information about the license -->

<!---LeetCode Topics Start-->
# LeetCode Topics
## Two Pointers
|  |
| ------- |
| [0005-longest-palindromic-substring](https://github.com/rishimule/leetcode-solutions/tree/master/0005-longest-palindromic-substring) |
| [0011-container-with-most-water](https://github.com/rishimule/leetcode-solutions/tree/master/0011-container-with-most-water) |
| [0042-trapping-rain-water](https://github.com/rishimule/leetcode-solutions/tree/master/0042-trapping-rain-water) |
| [0141-linked-list-cycle](https://github.com/rishimule/leetcode-solutions/tree/master/0141-linked-list-cycle) |
| [0160-intersection-of-two-linked-lists](https://github.com/rishimule/leetcode-solutions/tree/master/0160-intersection-of-two-linked-lists) |
| [0611-valid-triangle-number](https://github.com/rishimule/leetcode-solutions/tree/master/0611-valid-triangle-number) |
| [0647-palindromic-substrings](https://github.com/rishimule/leetcode-solutions/tree/master/0647-palindromic-substrings) |
## String
|  |
| ------- |
| [0003-longest-substring-without-repeating-characters](https://github.com/rishimule/leetcode-solutions/tree/master/0003-longest-substring-without-repeating-characters) |
| [0005-longest-palindromic-substring](https://github.com/rishimule/leetcode-solutions/tree/master/0005-longest-palindromic-substring) |
| [0013-roman-to-integer](https://github.com/rishimule/leetcode-solutions/tree/master/0013-roman-to-integer) |
| [0072-edit-distance](https://github.com/rishimule/leetcode-solutions/tree/master/0072-edit-distance) |
| [0139-word-break](https://github.com/rishimule/leetcode-solutions/tree/master/0139-word-break) |
| [0647-palindromic-substrings](https://github.com/rishimule/leetcode-solutions/tree/master/0647-palindromic-substrings) |
| [1047-remove-all-adjacent-duplicates-in-string](https://github.com/rishimule/leetcode-solutions/tree/master/1047-remove-all-adjacent-duplicates-in-string) |
| [1209-remove-all-adjacent-duplicates-in-string-ii](https://github.com/rishimule/leetcode-solutions/tree/master/1209-remove-all-adjacent-duplicates-in-string-ii) |
| [1347-minimum-number-of-steps-to-make-two-strings-anagram](https://github.com/rishimule/leetcode-solutions/tree/master/1347-minimum-number-of-steps-to-make-two-strings-anagram) |
## Dynamic Programming
|  |
| ------- |
| [0005-longest-palindromic-substring](https://github.com/rishimule/leetcode-solutions/tree/master/0005-longest-palindromic-substring) |
| [0042-trapping-rain-water](https://github.com/rishimule/leetcode-solutions/tree/master/0042-trapping-rain-water) |
| [0062-unique-paths](https://github.com/rishimule/leetcode-solutions/tree/master/0062-unique-paths) |
| [0063-unique-paths-ii](https://github.com/rishimule/leetcode-solutions/tree/master/0063-unique-paths-ii) |
| [0072-edit-distance](https://github.com/rishimule/leetcode-solutions/tree/master/0072-edit-distance) |
| [0121-best-time-to-buy-and-sell-stock](https://github.com/rishimule/leetcode-solutions/tree/master/0121-best-time-to-buy-and-sell-stock) |
| [0139-word-break](https://github.com/rishimule/leetcode-solutions/tree/master/0139-word-break) |
| [0647-palindromic-substrings](https://github.com/rishimule/leetcode-solutions/tree/master/0647-palindromic-substrings) |
| [0746-min-cost-climbing-stairs](https://github.com/rishimule/leetcode-solutions/tree/master/0746-min-cost-climbing-stairs) |
## Hash Table
|  |
| ------- |
| [0003-longest-substring-without-repeating-characters](https://github.com/rishimule/leetcode-solutions/tree/master/0003-longest-substring-without-repeating-characters) |
| [0013-roman-to-integer](https://github.com/rishimule/leetcode-solutions/tree/master/0013-roman-to-integer) |
| [0133-clone-graph](https://github.com/rishimule/leetcode-solutions/tree/master/0133-clone-graph) |
| [0139-word-break](https://github.com/rishimule/leetcode-solutions/tree/master/0139-word-break) |
| [0141-linked-list-cycle](https://github.com/rishimule/leetcode-solutions/tree/master/0141-linked-list-cycle) |
| [0160-intersection-of-two-linked-lists](https://github.com/rishimule/leetcode-solutions/tree/master/0160-intersection-of-two-linked-lists) |
| [0268-missing-number](https://github.com/rishimule/leetcode-solutions/tree/master/0268-missing-number) |
| [0380-insert-delete-getrandom-o1](https://github.com/rishimule/leetcode-solutions/tree/master/0380-insert-delete-getrandom-o1) |
| [1347-minimum-number-of-steps-to-make-two-strings-anagram](https://github.com/rishimule/leetcode-solutions/tree/master/1347-minimum-number-of-steps-to-make-two-strings-anagram) |
| [3507-minimum-pair-removal-to-sort-array-i](https://github.com/rishimule/leetcode-solutions/tree/master/3507-minimum-pair-removal-to-sort-array-i) |
## Depth-First Search
|  |
| ------- |
| [0098-validate-binary-search-tree](https://github.com/rishimule/leetcode-solutions/tree/master/0098-validate-binary-search-tree) |
| [0104-maximum-depth-of-binary-tree](https://github.com/rishimule/leetcode-solutions/tree/master/0104-maximum-depth-of-binary-tree) |
| [0133-clone-graph](https://github.com/rishimule/leetcode-solutions/tree/master/0133-clone-graph) |
| [0200-number-of-islands](https://github.com/rishimule/leetcode-solutions/tree/master/0200-number-of-islands) |
| [0226-invert-binary-tree](https://github.com/rishimule/leetcode-solutions/tree/master/0226-invert-binary-tree) |
| [0430-flatten-a-multilevel-doubly-linked-list](https://github.com/rishimule/leetcode-solutions/tree/master/0430-flatten-a-multilevel-doubly-linked-list) |
## Breadth-First Search
|  |
| ------- |
| [0104-maximum-depth-of-binary-tree](https://github.com/rishimule/leetcode-solutions/tree/master/0104-maximum-depth-of-binary-tree) |
| [0133-clone-graph](https://github.com/rishimule/leetcode-solutions/tree/master/0133-clone-graph) |
| [0200-number-of-islands](https://github.com/rishimule/leetcode-solutions/tree/master/0200-number-of-islands) |
| [0226-invert-binary-tree](https://github.com/rishimule/leetcode-solutions/tree/master/0226-invert-binary-tree) |
## Graph
|  |
| ------- |
| [0133-clone-graph](https://github.com/rishimule/leetcode-solutions/tree/master/0133-clone-graph) |
## Array
|  |
| ------- |
| [0004-median-of-two-sorted-arrays](https://github.com/rishimule/leetcode-solutions/tree/master/0004-median-of-two-sorted-arrays) |
| [0011-container-with-most-water](https://github.com/rishimule/leetcode-solutions/tree/master/0011-container-with-most-water) |
| [0042-trapping-rain-water](https://github.com/rishimule/leetcode-solutions/tree/master/0042-trapping-rain-water) |
| [0056-merge-intervals](https://github.com/rishimule/leetcode-solutions/tree/master/0056-merge-intervals) |
| [0063-unique-paths-ii](https://github.com/rishimule/leetcode-solutions/tree/master/0063-unique-paths-ii) |
| [0078-subsets](https://github.com/rishimule/leetcode-solutions/tree/master/0078-subsets) |
| [0121-best-time-to-buy-and-sell-stock](https://github.com/rishimule/leetcode-solutions/tree/master/0121-best-time-to-buy-and-sell-stock) |
| [0136-single-number](https://github.com/rishimule/leetcode-solutions/tree/master/0136-single-number) |
| [0139-word-break](https://github.com/rishimule/leetcode-solutions/tree/master/0139-word-break) |
| [0200-number-of-islands](https://github.com/rishimule/leetcode-solutions/tree/master/0200-number-of-islands) |
| [0268-missing-number](https://github.com/rishimule/leetcode-solutions/tree/master/0268-missing-number) |
| [0380-insert-delete-getrandom-o1](https://github.com/rishimule/leetcode-solutions/tree/master/0380-insert-delete-getrandom-o1) |
| [0611-valid-triangle-number](https://github.com/rishimule/leetcode-solutions/tree/master/0611-valid-triangle-number) |
| [0746-min-cost-climbing-stairs](https://github.com/rishimule/leetcode-solutions/tree/master/0746-min-cost-climbing-stairs) |
| [0875-koko-eating-bananas](https://github.com/rishimule/leetcode-solutions/tree/master/0875-koko-eating-bananas) |
| [1029-two-city-scheduling](https://github.com/rishimule/leetcode-solutions/tree/master/1029-two-city-scheduling) |
| [1823-find-the-winner-of-the-circular-game](https://github.com/rishimule/leetcode-solutions/tree/master/1823-find-the-winner-of-the-circular-game) |
| [2943-maximize-area-of-square-hole-in-grid](https://github.com/rishimule/leetcode-solutions/tree/master/2943-maximize-area-of-square-hole-in-grid) |
| [3147-taking-maximum-energy-from-the-mystic-dungeon](https://github.com/rishimule/leetcode-solutions/tree/master/3147-taking-maximum-energy-from-the-mystic-dungeon) |
| [3507-minimum-pair-removal-to-sort-array-i](https://github.com/rishimule/leetcode-solutions/tree/master/3507-minimum-pair-removal-to-sort-array-i) |
## Greedy
|  |
| ------- |
| [0011-container-with-most-water](https://github.com/rishimule/leetcode-solutions/tree/master/0011-container-with-most-water) |
| [0611-valid-triangle-number](https://github.com/rishimule/leetcode-solutions/tree/master/0611-valid-triangle-number) |
| [1029-two-city-scheduling](https://github.com/rishimule/leetcode-solutions/tree/master/1029-two-city-scheduling) |
## Trie
|  |
| ------- |
| [0139-word-break](https://github.com/rishimule/leetcode-solutions/tree/master/0139-word-break) |
## Memoization
|  |
| ------- |
| [0139-word-break](https://github.com/rishimule/leetcode-solutions/tree/master/0139-word-break) |
## Linked List
|  |
| ------- |
| [0002-add-two-numbers](https://github.com/rishimule/leetcode-solutions/tree/master/0002-add-two-numbers) |
| [0021-merge-two-sorted-lists](https://github.com/rishimule/leetcode-solutions/tree/master/0021-merge-two-sorted-lists) |
| [0141-linked-list-cycle](https://github.com/rishimule/leetcode-solutions/tree/master/0141-linked-list-cycle) |
| [0160-intersection-of-two-linked-lists](https://github.com/rishimule/leetcode-solutions/tree/master/0160-intersection-of-two-linked-lists) |
| [0430-flatten-a-multilevel-doubly-linked-list](https://github.com/rishimule/leetcode-solutions/tree/master/0430-flatten-a-multilevel-doubly-linked-list) |
| [3507-minimum-pair-removal-to-sort-array-i](https://github.com/rishimule/leetcode-solutions/tree/master/3507-minimum-pair-removal-to-sort-array-i) |
## Math
|  |
| ------- |
| [0002-add-two-numbers](https://github.com/rishimule/leetcode-solutions/tree/master/0002-add-two-numbers) |
| [0007-reverse-integer](https://github.com/rishimule/leetcode-solutions/tree/master/0007-reverse-integer) |
| [0009-palindrome-number](https://github.com/rishimule/leetcode-solutions/tree/master/0009-palindrome-number) |
| [0013-roman-to-integer](https://github.com/rishimule/leetcode-solutions/tree/master/0013-roman-to-integer) |
| [0050-powx-n](https://github.com/rishimule/leetcode-solutions/tree/master/0050-powx-n) |
| [0062-unique-paths](https://github.com/rishimule/leetcode-solutions/tree/master/0062-unique-paths) |
| [0268-missing-number](https://github.com/rishimule/leetcode-solutions/tree/master/0268-missing-number) |
| [0380-insert-delete-getrandom-o1](https://github.com/rishimule/leetcode-solutions/tree/master/0380-insert-delete-getrandom-o1) |
| [1823-find-the-winner-of-the-circular-game](https://github.com/rishimule/leetcode-solutions/tree/master/1823-find-the-winner-of-the-circular-game) |
## Binary Search
|  |
| ------- |
| [0004-median-of-two-sorted-arrays](https://github.com/rishimule/leetcode-solutions/tree/master/0004-median-of-two-sorted-arrays) |
| [0268-missing-number](https://github.com/rishimule/leetcode-solutions/tree/master/0268-missing-number) |
| [0611-valid-triangle-number](https://github.com/rishimule/leetcode-solutions/tree/master/0611-valid-triangle-number) |
| [0875-koko-eating-bananas](https://github.com/rishimule/leetcode-solutions/tree/master/0875-koko-eating-bananas) |
## Bit Manipulation
|  |
| ------- |
| [0078-subsets](https://github.com/rishimule/leetcode-solutions/tree/master/0078-subsets) |
| [0136-single-number](https://github.com/rishimule/leetcode-solutions/tree/master/0136-single-number) |
| [0268-missing-number](https://github.com/rishimule/leetcode-solutions/tree/master/0268-missing-number) |
## Sorting
|  |
| ------- |
| [0056-merge-intervals](https://github.com/rishimule/leetcode-solutions/tree/master/0056-merge-intervals) |
| [0268-missing-number](https://github.com/rishimule/leetcode-solutions/tree/master/0268-missing-number) |
| [0611-valid-triangle-number](https://github.com/rishimule/leetcode-solutions/tree/master/0611-valid-triangle-number) |
| [1029-two-city-scheduling](https://github.com/rishimule/leetcode-solutions/tree/master/1029-two-city-scheduling) |
| [2943-maximize-area-of-square-hole-in-grid](https://github.com/rishimule/leetcode-solutions/tree/master/2943-maximize-area-of-square-hole-in-grid) |
## Stack
|  |
| ------- |
| [0042-trapping-rain-water](https://github.com/rishimule/leetcode-solutions/tree/master/0042-trapping-rain-water) |
| [0155-min-stack](https://github.com/rishimule/leetcode-solutions/tree/master/0155-min-stack) |
| [1047-remove-all-adjacent-duplicates-in-string](https://github.com/rishimule/leetcode-solutions/tree/master/1047-remove-all-adjacent-duplicates-in-string) |
| [1209-remove-all-adjacent-duplicates-in-string-ii](https://github.com/rishimule/leetcode-solutions/tree/master/1209-remove-all-adjacent-duplicates-in-string-ii) |
## Monotonic Stack
|  |
| ------- |
| [0042-trapping-rain-water](https://github.com/rishimule/leetcode-solutions/tree/master/0042-trapping-rain-water) |
## Design
|  |
| ------- |
| [0155-min-stack](https://github.com/rishimule/leetcode-solutions/tree/master/0155-min-stack) |
| [0380-insert-delete-getrandom-o1](https://github.com/rishimule/leetcode-solutions/tree/master/0380-insert-delete-getrandom-o1) |
## Randomized
|  |
| ------- |
| [0380-insert-delete-getrandom-o1](https://github.com/rishimule/leetcode-solutions/tree/master/0380-insert-delete-getrandom-o1) |
## Union Find
|  |
| ------- |
| [0200-number-of-islands](https://github.com/rishimule/leetcode-solutions/tree/master/0200-number-of-islands) |
## Matrix
|  |
| ------- |
| [0063-unique-paths-ii](https://github.com/rishimule/leetcode-solutions/tree/master/0063-unique-paths-ii) |
| [0200-number-of-islands](https://github.com/rishimule/leetcode-solutions/tree/master/0200-number-of-islands) |
## Doubly-Linked List
|  |
| ------- |
| [0430-flatten-a-multilevel-doubly-linked-list](https://github.com/rishimule/leetcode-solutions/tree/master/0430-flatten-a-multilevel-doubly-linked-list) |
| [3507-minimum-pair-removal-to-sort-array-i](https://github.com/rishimule/leetcode-solutions/tree/master/3507-minimum-pair-removal-to-sort-array-i) |
## Sliding Window
|  |
| ------- |
| [0003-longest-substring-without-repeating-characters](https://github.com/rishimule/leetcode-solutions/tree/master/0003-longest-substring-without-repeating-characters) |
## Recursion
|  |
| ------- |
| [0002-add-two-numbers](https://github.com/rishimule/leetcode-solutions/tree/master/0002-add-two-numbers) |
| [0021-merge-two-sorted-lists](https://github.com/rishimule/leetcode-solutions/tree/master/0021-merge-two-sorted-lists) |
| [0050-powx-n](https://github.com/rishimule/leetcode-solutions/tree/master/0050-powx-n) |
| [1823-find-the-winner-of-the-circular-game](https://github.com/rishimule/leetcode-solutions/tree/master/1823-find-the-winner-of-the-circular-game) |
## Tree
|  |
| ------- |
| [0098-validate-binary-search-tree](https://github.com/rishimule/leetcode-solutions/tree/master/0098-validate-binary-search-tree) |
| [0104-maximum-depth-of-binary-tree](https://github.com/rishimule/leetcode-solutions/tree/master/0104-maximum-depth-of-binary-tree) |
| [0226-invert-binary-tree](https://github.com/rishimule/leetcode-solutions/tree/master/0226-invert-binary-tree) |
## Binary Search Tree
|  |
| ------- |
| [0098-validate-binary-search-tree](https://github.com/rishimule/leetcode-solutions/tree/master/0098-validate-binary-search-tree) |
## Binary Tree
|  |
| ------- |
| [0098-validate-binary-search-tree](https://github.com/rishimule/leetcode-solutions/tree/master/0098-validate-binary-search-tree) |
| [0104-maximum-depth-of-binary-tree](https://github.com/rishimule/leetcode-solutions/tree/master/0104-maximum-depth-of-binary-tree) |
| [0226-invert-binary-tree](https://github.com/rishimule/leetcode-solutions/tree/master/0226-invert-binary-tree) |
## Queue
|  |
| ------- |
| [1823-find-the-winner-of-the-circular-game](https://github.com/rishimule/leetcode-solutions/tree/master/1823-find-the-winner-of-the-circular-game) |
## Simulation
|  |
| ------- |
| [1823-find-the-winner-of-the-circular-game](https://github.com/rishimule/leetcode-solutions/tree/master/1823-find-the-winner-of-the-circular-game) |
| [3507-minimum-pair-removal-to-sort-array-i](https://github.com/rishimule/leetcode-solutions/tree/master/3507-minimum-pair-removal-to-sort-array-i) |
## Heap (Priority Queue)
|  |
| ------- |
| [3507-minimum-pair-removal-to-sort-array-i](https://github.com/rishimule/leetcode-solutions/tree/master/3507-minimum-pair-removal-to-sort-array-i) |
## Ordered Set
|  |
| ------- |
| [3507-minimum-pair-removal-to-sort-array-i](https://github.com/rishimule/leetcode-solutions/tree/master/3507-minimum-pair-removal-to-sort-array-i) |
## Prefix Sum
|  |
| ------- |
| [3147-taking-maximum-energy-from-the-mystic-dungeon](https://github.com/rishimule/leetcode-solutions/tree/master/3147-taking-maximum-energy-from-the-mystic-dungeon) |
## Divide and Conquer
|  |
| ------- |
| [0004-median-of-two-sorted-arrays](https://github.com/rishimule/leetcode-solutions/tree/master/0004-median-of-two-sorted-arrays) |
## Combinatorics
|  |
| ------- |
| [0062-unique-paths](https://github.com/rishimule/leetcode-solutions/tree/master/0062-unique-paths) |
## Counting
|  |
| ------- |
| [1347-minimum-number-of-steps-to-make-two-strings-anagram](https://github.com/rishimule/leetcode-solutions/tree/master/1347-minimum-number-of-steps-to-make-two-strings-anagram) |
## Backtracking
|  |
| ------- |
| [0078-subsets](https://github.com/rishimule/leetcode-solutions/tree/master/0078-subsets) |
<!---LeetCode Topics End-->