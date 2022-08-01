"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran = sorted(list(ransomNote))
        mag = sorted(list(magazine))
        
        for char in mag:
            if ran and char == ran[0]:
                ran.pop(0)
                
        if ran:
            return False
        else:
            return True
          
          
# Alternative solution:

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(ransomNote) > len(magazine):
            return False
        
        r_counter = Counter(ransomNote)
        m_counter = Counter(magazine)
        
        for i in range(len(ransomNote)):
            if ransomNote[i] not in magazine:
                return False
            elif r_counter[ransomNote[i]] > m_counter[ransomNote[i]]:
                return False
        return True
