"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()
        
        for index, value in enumerate(nums):
            remaining_number = target - value
            
            if remaining_number in hash_map:
                return [hash_map[remaining_number], index]
            
            hash_map[value]=index
            
            
            
# Alternative solution:            
      class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()
        
        for i in range(len(nums)):
            num = nums[i]
            remaining_number = target - num
            
            if num in hash_map:
                return[hash_map[num],i]
            else:
                hash_map[remaining_number] = i 
            
          
 # a very slow solution:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
           for j in range(i+1, len(nums)):
            sum = nums[i] +  nums[j]
            if sum == target:
                return [i,j]
            
          
