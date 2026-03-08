from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_length, p_length = len(s), len(p)

        if p_length > s_length:
            return []

        s_count = Counter(s[: p_length - 1])
        p_count = Counter(p)
        res = []

        if s_count == p_count:
            res.append(0)

        for i in range(p_length - 1, s_length):
            s_count[s[i]] += 1

            if s_count == p_count:
                res.append(i - p_length + 1)

            left_char = s[i - p_length + 1]
            s_count[left_char] -= 1

            if s_count[left_char] == 0:
                del s_count[left_char]

        return res


if __name__ == "__main__":
    sol = Solution()
    test_cases = [("cbaebabacd", "abc"), ("abab", "ab")]

    for text, pattern in test_cases:
        print(f"Anagrams: {sol.findAnagrams(text, pattern)}")
