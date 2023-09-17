'''7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = 0
        result = 0
        minus = False
        if x < 0:
            minus = True
            x = x * -1
        while(x > 0):
            y = x % 10
            x = int(x /10)
            result = result * 10 + y
        if minus == True:
            result = result * -1
        if result < -2147483648 or result > 2147483647:
            result = 0
        return result
x = 123456789101
a = 123
b = 12321
sol = Solution()
y = sol.reverse(x)
print(y)
y = sol.reverse(a)
print(y)
y = sol.reverse(b)
print(y)