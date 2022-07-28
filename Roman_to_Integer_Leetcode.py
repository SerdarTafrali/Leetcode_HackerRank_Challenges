"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol = Value: I=1, V=5, X=10, L=50, C=100, D=500, M=1000

For example, 2 is written as II in Roman numeral, just two ones added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Examples:

Input: s = "III"       |Input: s = "LVIII"                  |Input: s = "MCMXCIV"
Output: 3              |Output: 58                          |Output: 1994
Explanation: III = 3.  |Explanation: L = 50, V= 5, III = 3. |Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"""

class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        N = len(s)
        i = N-1
        output= 0
        while i >= 0:
            if i < N-1 and hashmap[s[i]] < hashmap[s[i+1]]:
                output -= hashmap[s[i]]
            else:
                output += hashmap[s[i]]
            i-=1
            
        return output
