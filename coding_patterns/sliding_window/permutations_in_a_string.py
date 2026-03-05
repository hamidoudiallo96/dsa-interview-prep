from collections import Counter


class Solution:
    def findPermutation(self, text: str, pattern: str) -> bool:
        if len(pattern) > len(text):
            return False

        char_count = Counter(pattern)
        chars_needed = len(char_count)
        start = 0
        n = len(text)

        for end in range(n):
            right_char = text[end]

            char_count[right_char] -= 1

            if char_count[right_char] == 0:
                chars_needed -= 1

            window_size = end - start + 1

            if window_size > len(pattern):
                left_char = text[start]

                char_count[left_char] += 1

                if char_count[left_char] == 1:
                    chars_needed += 1

                start += 1

            if chars_needed == 0:
                return True

        return False


if __name__ == "__main__":
    sol = Solution()
    input_data = [
        ("oidbcaf", "abc"),
        ("odicf", "dc"),
        ("bcdxabcdy", "bcdyabcdx"),
        ("aaacb", "abc"),
        ("eidbaooo", "ab"),
        ("eidboaoo", "ab")
    ]
    for text, pattern in input_data:
        print(f"Pattern Found: {sol.findPermutation(text, pattern)}")
