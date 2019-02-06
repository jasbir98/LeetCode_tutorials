""" Input:
Link: https://leetcode.com/problems/palindrome-number/

n : An Integer
n = int(input())
"""


class Solution:
    """ Time Complexity: O(logn) [Here base is 10 as the number is a decimal number]
        Space Complexity: O(1)
     """
    def isPalindrome(self, x):
        x = str(x)
        return x == x[::-1]

