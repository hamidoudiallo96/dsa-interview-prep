# Problem Statement

# Given an array of unsorted numbers and a target number, find all unique
# quadruplets in it, whose sum is equal to the target number.

# Example 1:
# Input: [4, 1, 2, -1, 1, -3], target = 1
# Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
# Explanation: Both the quadruplets add up to the target.


# Example 2:
# Input: [2, 0, -1, 1, -2, 2], target = 2
# Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
# Explanation: Both the quadruplets add up to the target.

# Constraints:
# 1 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109


class Solution:
    def search_quadruplets(self, arr, target):
        n = len(arr)
        quads = []

        if n < 2:
            return []

        arr.sort()

        for i in range(n-3):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            for j in range(i + 1, n-2):
                if j > 0 and arr[j] == arr[j-1]:
                    continue

                left, right = j + 1, n - 1

                while left < right:
                    current_sum = arr[i] + arr[j] + arr[left] + arr[right]

                    if current_sum == target:
                        quads.append([arr[i], arr[j], arr[left], arr[right]])
                        left += 1
                        right -= 1

                        while left < right and arr[left] == arr[left-1]:
                            left += 1

                        while left < right and arr[right] == arr[right + 1]:
                            right -= 1
                    elif current_sum < target:
                        left += 1
                    elif current_sum > target:
                        right -= 1

        return quads


if __name__ == "__main__":
    sol = Solution()
    quad1 = sol.search_quadruplets([4, 1, 2, -1, 1, -3], 1)
    quad2 = sol.search_quadruplets([2, 0, -1, 1, -2, 2], 2)

    print(f"Quad1: {quad1}")
    print(f"Quad2: {quad2}")
