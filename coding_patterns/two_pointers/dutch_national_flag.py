# Problem Statement
# Given an array containing 0s, 1s and 2s, sort the array in-place.
# You should treat numbers of the array as objects, hence,
# we can’t count 0s, 1s, and 2s to recreate the array.

# The flag of the Netherlands consists of three colors:
# red, white and blue; and since our input array also
# consists of three different numbers that is why it is
# called Dutch National Flag problem.

# Examples

# Example 1
# Input: arr = [1, 0, 2, 1, 0]
# Output: [0, 0, 1, 1, 2]
# Explanation:
# All 0s are moved to the front, 1s in the middle, and 2s at the end.
# The relative order within each group doesn't matter.


# Example 2
# Input: arr= [2, 2, 0, 1, 2, 0]
# Output: [0, 0, 1, 2, 2, 2]
# Explanation:
# All 0s come first, followed by the 1, and then all 2s at the end.
# Sorting is done in-place without using extra space or counting.

# Constraints:
# n == arr.length
# 1 <= n <= 300
# arr[i] is either 0, 1, or 2.


class Solution:
    def sort_flags(self, arr):
        red, white, blue = 0, 1, 2
        lo = curr = 0
        hi = len(arr) - 1

        while curr <= hi:
            if arr[curr] == red:
                arr[lo], arr[curr] = arr[curr], arr[lo]
                lo += 1
                curr += 1
            elif arr[curr] == white:
                curr += 1
            elif arr[curr] == blue:
                arr[curr], arr[hi] = arr[hi], arr[curr]
                hi -= 1

        return arr


if __name__ == "__main__":
    sol = Solution()

    arr = [1, 0, 2, 1, 0]
    arr1 = [2, 2, 0, 1, 2, 0]

    print(sol.sort_flags(arr))
    print(sol.sort_flags(arr1))
