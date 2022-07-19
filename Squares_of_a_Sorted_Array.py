"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        nums[0] = nums[0]**2
        for i in range(1,len(nums)):
            nums[i] = nums[i]**2
            
        nums = sorted(nums)
        return nums
