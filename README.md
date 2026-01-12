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
| [0647-palindromic-substrings](https://github.com/rishimule/leetcode-solutions/tree/master/0647-palindromic-substrings) |
## String
|  |
| ------- |
| [0005-longest-palindromic-substring](https://github.com/rishimule/leetcode-solutions/tree/master/0005-longest-palindromic-substring) |
| [0139-word-break](https://github.com/rishimule/leetcode-solutions/tree/master/0139-word-break) |
| [0647-palindromic-substrings](https://github.com/rishimule/leetcode-solutions/tree/master/0647-palindromic-substrings) |
## Dynamic Programming
|  |
| ------- |
| [0005-longest-palindromic-substring](https://github.com/rishimule/leetcode-solutions/tree/master/0005-longest-palindromic-substring) |
| [0042-trapping-rain-water](https://github.com/rishimule/leetcode-solutions/tree/master/0042-trapping-rain-water) |
| [0139-word-break](https://github.com/rishimule/leetcode-solutions/tree/master/0139-word-break) |
| [0647-palindromic-substrings](https://github.com/rishimule/leetcode-solutions/tree/master/0647-palindromic-substrings) |
## Hash Table
|  |
| ------- |
| [0133-clone-graph](https://github.com/rishimule/leetcode-solutions/tree/master/0133-clone-graph) |
| [0139-word-break](https://github.com/rishimule/leetcode-solutions/tree/master/0139-word-break) |
| [0141-linked-list-cycle](https://github.com/rishimule/leetcode-solutions/tree/master/0141-linked-list-cycle) |
| [0268-missing-number](https://github.com/rishimule/leetcode-solutions/tree/master/0268-missing-number) |
| [0380-insert-delete-getrandom-o1](https://github.com/rishimule/leetcode-solutions/tree/master/0380-insert-delete-getrandom-o1) |
## Depth-First Search
|  |
| ------- |
| [0133-clone-graph](https://github.com/rishimule/leetcode-solutions/tree/master/0133-clone-graph) |
| [0200-number-of-islands](https://github.com/rishimule/leetcode-solutions/tree/master/0200-number-of-islands) |
## Breadth-First Search
|  |
| ------- |
| [0133-clone-graph](https://github.com/rishimule/leetcode-solutions/tree/master/0133-clone-graph) |
| [0200-number-of-islands](https://github.com/rishimule/leetcode-solutions/tree/master/0200-number-of-islands) |
## Graph
|  |
| ------- |
| [0133-clone-graph](https://github.com/rishimule/leetcode-solutions/tree/master/0133-clone-graph) |
## Array
|  |
| ------- |
| [0011-container-with-most-water](https://github.com/rishimule/leetcode-solutions/tree/master/0011-container-with-most-water) |
| [0042-trapping-rain-water](https://github.com/rishimule/leetcode-solutions/tree/master/0042-trapping-rain-water) |
| [0136-single-number](https://github.com/rishimule/leetcode-solutions/tree/master/0136-single-number) |
| [0139-word-break](https://github.com/rishimule/leetcode-solutions/tree/master/0139-word-break) |
| [0200-number-of-islands](https://github.com/rishimule/leetcode-solutions/tree/master/0200-number-of-islands) |
| [0268-missing-number](https://github.com/rishimule/leetcode-solutions/tree/master/0268-missing-number) |
| [0380-insert-delete-getrandom-o1](https://github.com/rishimule/leetcode-solutions/tree/master/0380-insert-delete-getrandom-o1) |
## Greedy
|  |
| ------- |
| [0011-container-with-most-water](https://github.com/rishimule/leetcode-solutions/tree/master/0011-container-with-most-water) |
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
| [0141-linked-list-cycle](https://github.com/rishimule/leetcode-solutions/tree/master/0141-linked-list-cycle) |
## Math
|  |
| ------- |
| [0268-missing-number](https://github.com/rishimule/leetcode-solutions/tree/master/0268-missing-number) |
| [0380-insert-delete-getrandom-o1](https://github.com/rishimule/leetcode-solutions/tree/master/0380-insert-delete-getrandom-o1) |
## Binary Search
|  |
| ------- |
| [0268-missing-number](https://github.com/rishimule/leetcode-solutions/tree/master/0268-missing-number) |
## Bit Manipulation
|  |
| ------- |
| [0136-single-number](https://github.com/rishimule/leetcode-solutions/tree/master/0136-single-number) |
| [0268-missing-number](https://github.com/rishimule/leetcode-solutions/tree/master/0268-missing-number) |
## Sorting
|  |
| ------- |
| [0268-missing-number](https://github.com/rishimule/leetcode-solutions/tree/master/0268-missing-number) |
## Stack
|  |
| ------- |
| [0042-trapping-rain-water](https://github.com/rishimule/leetcode-solutions/tree/master/0042-trapping-rain-water) |
## Monotonic Stack
|  |
| ------- |
| [0042-trapping-rain-water](https://github.com/rishimule/leetcode-solutions/tree/master/0042-trapping-rain-water) |
## Design
|  |
| ------- |
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
| [0200-number-of-islands](https://github.com/rishimule/leetcode-solutions/tree/master/0200-number-of-islands) |
<!---LeetCode Topics End-->