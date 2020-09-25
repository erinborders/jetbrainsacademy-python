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
            if item in matches.values():
                # return the index of item and pair
                # but what if the item and match are the same number ?
                firstIndex = array.index(item)
                return [firstIndex, array.index(pair, firstIndex)]
            # otherwise add pair to dict
            matches.update({item: pair})
        # if you get to this point, there are no matches in the array so end it
        return None 

## ACCEPTED ANSWER WITH TEST CASES

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create dict for storing pairs
        matches = {}
        # loop through list
        for item in nums:
            # would check if numbers were greater than target but target could be negative
            # find the complement to the number we're on
            pair = target - item 
            # check if dict already has pair
            if item in matches.values():
                # return the index of item and pair
                firstIndex = nums.index(item)
                if item == pair:
                    # if they're the same number, find the next index
                    secondIndex = nums.index(pair, firstIndex+1)
                else:
                    # otherwise, secondIndex is the pair 
                    secondIndex = nums.index(pair)
                return [firstIndex, secondIndex]
            # otherwise add pair to dict
            matches.update({item: pair})
        # if you get to this point, there are no matches in the list so end it
        return None 

# 2. Reverse integer

# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit 
# signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your 
# function returns 0 when the reversed integer overflows.
            
            

            