'''
@Author: 拎把木剑当大侠
@Description: 
@Date: 2019-05-07 23:27:07
@LastEditTime: 2019-05-07 23:41:17
'''


class Solution(object):
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        n = len(A)

        def guess(m):
            a = b = None
            c = n
            res = 0
            for r in range(n-1, 0, -1):
                c = min(c, r-1)
                tar = A[r]*m
                while c >= 0 and A[c] > tar:
                    c -= 1
                res += c+1
                if c >= 0 and (a == None or a*A[r] < A[c]*b):
                    a = A[c]
                    b = A[r]
            return res, a, b
        l, r = 0, 1
        while l < r:
            mid = (l+r)/2.0
            d, a, b = guess(mid)
            if d > K:
                r = mid
            elif d < K:
                l = mid
            else:
                return a, b
