# Problem : Longest substring without repeating characters
# Leetcode link https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      
        max_length_substring = 0
        substring = ""
        for i in s:
            if i not in substring:
                substring += i
                max_length_substring = max(max_length_substring, len(substring))
            else:
                
                substring = substring[substring.index(i)+1:] + i
        return max_length_substring
                
        
        
