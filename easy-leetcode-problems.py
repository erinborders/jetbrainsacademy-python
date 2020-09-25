# 1. Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 105
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create dict for storing pairs
        matches = {}
        # loop through list
        for item in array:
            # would check if numbers were greater than target but target could be negative
            # find the complement to the number we're on
            pair = target - item 
            # check if dict already has pair
            if pair in matches:
                # return the index of item and pair
                return [array.index(item), array.index(pair)]
            # otherwise add pair to dict
            matches.update({item: pair})
        # if you get to this point, there are no matches in the array so end it
        return None 
            
            

            