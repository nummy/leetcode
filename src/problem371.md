Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

Credits:
Special thanks to @fujiaozhu for adding this problem and creating all test cases.

Subscribe to see which companies asked this question

Solution:

```python
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        sum = a^b
        carry = a&b<<1
        while carry != 0:
            num1 = sum
            num2 = carry
            sum = num1^num2
            carry = num1&num2<<1
        return sum
        
```
