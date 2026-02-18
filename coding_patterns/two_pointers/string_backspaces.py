# Problem Statement
# Given two strings containing backspaces (identified by the character ‘#’),
# check if the two strings are equal.

# Example 1:
# Input: str1="xy#z", str2="xzz#"
# Output: true
# Explanation:
# After applying backspaces the strings become "xz" and "xz" respectively.

# Example 2:
# Input: str1="xy#z", str2="xyz#"
# Output: false
# Explanation:
# After applying backspaces the strings become "xz" and "xy" respectively.

# Example 3:
# Input: str1="xp#", str2="xyz##"
# Output: true
# Explanation:
# After applying backspaces the strings become "x" and "x" respectively.
# In "xyz##", the first '#' removes the character 'z' and the second '#'
# removes the character 'y'.

# Example 4:
# Input: str1="xywrrmp", str2="xywrrmu#p"
# Output: true
# Explanation:
# After applying backspaces the strings become
# "xywrrmp" and "xywrrmp" respectively.

# Constraints:
# 1 <= str1.length, str2.length <= 200
# str1 and str2 only contain lowercase letters and '#' characters.


class Solution:
    def compare(self, str1, str2):
        def next_valid_char(word, idx):
            backspaces = 0

            while idx >= 0:
                if word[idx] == "#":
                    backspaces += 1
                elif backspaces > 0:
                    backspaces -= 1
                else:
                    break

                idx -= 1

            return idx

        s1 = len(str1) - 1
        s2 = len(str2) - 1

        while s1 >= 0 or s2 >= 0:
            p1 = next_valid_char(str1, s1)
            p2 = next_valid_char(str2, s2)

            if p1 < 0 and p2 < 0:
                return True

            if p1 < 0 or p2 < 0:
                return False

            if str1[p1] != str2[p2]:
                return False

            s1 = p1 - 1
            s2 = p2 - 1

        return True


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("xy#z", "xzz#"),
        ("xy#z", "xyz#"),
        ("xp#", "xyz##"),
        ("xywrrmp", "xywrrmu#p")
    ]

    for test_case in test_cases:
        str1, str2 = test_case
        print(sol.compare(str1, str2))
