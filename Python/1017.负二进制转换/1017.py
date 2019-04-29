'''
@Author: 拎把木剑当大侠
@Description: 
@Date: 2019-04-29 14:20:01
@LastEditTime: 2019-04-29 14:20:10
'''


class Solution(object):
    def baseNeg2(self, N):
        """
        :type N: int
        :rtype: str
        """
        res = ''
        while True:
            res = str(N % 2)+res
            N = -(N // 2)
            if (N == 0):
                break
        return res
