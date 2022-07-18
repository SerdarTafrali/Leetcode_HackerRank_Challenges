""" Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct. """

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        for i in range(1,len(nums)): 
            if nums[i] == nums[i-1]:
                return True
        return False
