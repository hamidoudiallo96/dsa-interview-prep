# Problem Statement
# Given an array, find the length of the smallest
# subarray in it which when sorted will sort the whole array.

# Example 1:
# Input: [1, 2, 5, 3, 7, 10, 9, 12]
# Output: 5
# Explanation:
# We need to sort only the subarray[5, 3, 7, 10, 9]
# to make the whole array sorted

# Example 2:
# Input: [1, 3, 2, 0, -1, 7, 10]
# Output: 5
# Explanation:
# We need to sort only the subarray[1, 3, 2, 0, -1]
# to make the whole array sorted

# Example 3:
# Input: [1, 2, 3]
# Output: 0
# Explanation: The array is already sorted

# Example 4:
# Input: [3, 2, 1]
# Output: 3
# Explanation: The whole array needs to be sorted.


# Constraints:
# 1 <= arr.length <= 104
# -105 <= arr[i] <= 105


class Solution:
    def minimum_sort(self, arr):
        if len(arr) < 2:
            return 0

        n = len(arr)
        start, end = len(arr) - 1, 0
        min_v, max_v = float("inf"), float("-inf")

        for i in range(n):
            max_v = max(max_v, arr[i])
            if arr[i] < max_v:
                end = i

            j = n - 1 - i

            min_v = min(min_v, arr[j])
            if arr[j] > min_v:
                start = j

        if start >= end:
            return 0

        return end - start + 1


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1, 2, 5, 3, 7, 10, 9, 12],
        [1, 3, 2, 0, -1, 7, 10],
        [1, 2, 3],
        [3, 2, 1]
    ]

    for test_case in test_cases:
        print(sol.minimum_sort(test_case))
