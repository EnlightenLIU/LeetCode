'''
@Author: 拎把木剑当大侠
@Description:
@Date: 2019-04-14 16:40:07
@LastEditTime: 2019-04-14 16:48:41
'''


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = int(input('输入:'))
        n = bin(n)
        return n.count('1')
