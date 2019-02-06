""" Input:
Link: https://leetcode.com/problems/two-sum/

n : Number of Elements in the List
nums : List of n elements
target : Target Element

n = int(input())
nums = [int(x) for x in input().split()]
target = int(input())

"""

class Solution:
    # Time Complexity : O(n)
    # Space Complexity : O(n)
    
    def twoSum(self, nums, target):
        mydict = {}
        for i in range(len(nums)):
            if target - nums[i] in mydict and mydict[target - nums[i]]!=i:
                return [i,mydict[target-nums[i]]]
            mydict[nums[i]] = i

