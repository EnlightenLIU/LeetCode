'''
@Author: 拎把木剑当大侠
@Description: 
@Date: 2019-04-16 15:17:43
@LastEditTime: 2019-04-16 16:03:56
'''


class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        m = 0
        n = len(chars)
        cur = 0
        while m < n:
            k = m
            while k < n-1 and chars[k] == chars[k+1]:
                k += 1
            chars[cur] = chars[m]
            cur += 1
            if m != k:
                a = str(k-m+1)
                tlen = len(a)
                for i in range(tlen):
                    chars[cur+i] = a[i]
                cur += tlen
            m = k+1
        return cur
