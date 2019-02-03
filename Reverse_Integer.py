""" Input:
Link: https://leetcode.com/problems/reverse-integer/solution/

n : An Integer
n = int(input())
"""


class Solution:
    """ Time Complexity: O(logn) [Here base is 10 as the number is a decimal number]
        Space Complexity: O(1)

     """
    def reverse(self, x):
        ans = 0
        max_int = 2**31
        sign = (x > 0) - (x < 0)
        x = abs(x)
        while x!=0:
            ans = ans * 10 + x%10
            if ans > max_int -1 or ans < -max_int:
                return 0
            x = x//10
        return ans * sign

