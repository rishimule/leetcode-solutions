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

## Problem Categories

The problems are organized into the following categories:

- **Easy**  <!-- Category for easy problems -->
  - Problem 1: [Two Sum](https://leetcode.com/problems/two-sum/)  <!-- Example of an easy problem -->
  - Problem 2: [Reverse String](https://leetcode.com/problems/reverse-string/)  <!-- Another example of an easy problem -->

- **Medium**  <!-- Category for medium problems -->
  - Problem 1: [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)  <!-- Example of a medium problem -->
  - Problem 2: [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)  <!-- Another example of a medium problem -->

- **Hard**  <!-- Category for hard problems -->
  - Problem 1: [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)  <!-- Example of a hard problem -->
  - Problem 2: [N-Queens](https://leetcode.com/problems/n-queens/)  <!-- Another example of a hard problem -->

## Solution Format

Each solution is organized in a separate file named after the problem title, following this format:

```
<Problem_Title>.<language_extension>
```

### Example Structure
```
/Easy  <!-- Directory for easy problems -->
  ├── Two_Sum.py  <!-- Example solution file for Two Sum problem in Python -->
  ├── Reverse_String.py  <!-- Example solution file for Reverse String problem in Python -->
/Medium  <!-- Directory for medium problems -->
  ├── Add_Two_Numbers.java  <!-- Example solution file for Add Two Numbers problem in Java -->
  ├── Longest_Substring_Without_Repeating_Characters.cpp  <!-- Example solution file for Longest Substring problem in C++ -->
/Hard  <!-- Directory for hard problems -->
  ├── Median_of_Two_Sorted_Arrays.py  <!-- Example solution file for Median problem in Python -->
  ├── N-Queens.java  <!-- Example solution file for N-Queens problem in Java -->
```

## Example Problem

### Problem: Two Sum
- **Link**: [Two Sum](https://leetcode.com/problems/two-sum/)  <!-- Link to the problem -->
- **Description**: Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.  <!-- Description of the problem -->

#### Solution (Python)
```python
def two_sum(nums, target):
    num_map = {}  # Dictionary to store the index of the numbers
    for i, num in enumerate(nums):
        complement = target - num  # Calculate the complement
        if complement in num_map:  # Check if the complement exists
            return [num_map[complement], i]  # Return the indices if found
        num_map[num] = i  # Store the index of the number
```

#### Usage
```python
nums = [2, 7, 11, 15]  # Example input
target = 9  # Example target
result = two_sum(nums, target)  # Call the function
print(result)  # Output: [0, 1]  <!-- Expected output -->
```

## Contributing

Contributions are welcome! If you have solved a problem that is not yet included in this repository, please feel free to submit a pull request with your solution.  <!-- Invitation for others to contribute -->

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.  <!-- Information about the license -->
