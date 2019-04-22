'''
@Author: 拎把木剑当大侠
@Description: 
@Date: 2019-04-22 12:49:45
@LastEditTime: 2019-04-22 13:43:16
'''


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = m = 0
        dic = {0: 1}
        for i in nums:
            m += i
            if m-k in dic:
                result += dic[m-k]
            if m in dic:
                dic[m] += 1
            else:
                dic[m] = 1
        return result
