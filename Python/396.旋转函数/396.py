'''
@Author: 拎把木剑当大侠
@Description: 
@Date: 2019-04-24 21:50:35
@LastEditTime: 2019-04-24 22:35:14
'''


class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 主要是找到规律

        _sum = 0
        N = len(A)
        f = 0
        for i, a in enumerate(A):
            _sum += a
            f += i * a
        res = f
        for i in range(N - 1, 0, -1):
            f = f + _sum - N * A[i]
            res = max(res, f)
        return res
