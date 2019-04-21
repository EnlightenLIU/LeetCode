'''
@Author: 拎把木剑当大侠
@Description: 
@Date: 2019-04-21 13:29:25
@LastEditTime: 2019-04-21 13:31:57
'''
from math import sqrt


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        sums = 1
        for i in range(2, int(sqrt(num))+1):
            if num % i == 0:
                sums += i + num // i
        return sums == num
