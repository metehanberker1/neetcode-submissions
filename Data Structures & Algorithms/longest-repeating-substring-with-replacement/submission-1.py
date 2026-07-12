from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = k + 1
        chars = Counter(s[:j])
        max_window = k + 1

        while j < len(s):
            chars[s[j]] = chars.get(s[j], 0) + 1
            j += 1

            if max(chars.values()) + k >= j - i:
                max_window = max(max_window, j-i)
            else:
                chars[s[i]] = chars.get(s[i], 0) - 1
                i += 1

        return max_window

