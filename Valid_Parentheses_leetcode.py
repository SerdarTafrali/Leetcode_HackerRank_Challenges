"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {")":"(", "]":"[", "}":"{"}
        
        for p in s:
            if p in hashmap.values():
                stack.append(p)
            elif stack and hashmap[p] == stack[-1]:
                stack.pop()
            else:
                return False
            
        return stack == []
