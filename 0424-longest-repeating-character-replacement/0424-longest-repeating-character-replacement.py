class Solution:
    def characterReplacement(self, s, k):
        count = [0] * 26
        left = 0
        max_freq = 0
        max_length = 0

        for right in range(len(s)):
            count[ord(s[right]) - ord('A')] += 1
            
            max_freq = max(max_freq, count[ord(s[right]) - ord('A')])
            
            if (right - left + 1) - max_freq > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)

        return max_length