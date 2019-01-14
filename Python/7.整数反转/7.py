'''
@Author: 拎把木剑当大侠
@Description: 
@Date: 2019-01-10 16:39:40
@LastEditTime: 2019-01-11 14:57:34
'''


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if (x > 0):
            flag = 1
        else:
            flag = -1
        x = x*flag
        a = 0
        while(x):
            a = a*10+x % 10
            x = x//10
        return a*flag
