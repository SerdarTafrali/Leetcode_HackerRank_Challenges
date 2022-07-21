"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_s, t_s = [],[]
        
        for i in s:
            if i == "#":
                if s_s: s_s.pop()
            else:
                s_s.append(i)
                
        for i in t:
            if i == "#":
                if t_s: t_s.pop()
            else:
                t_s.append(i)
        
        if s_s == t_s:
            return True
        else:
            return False

