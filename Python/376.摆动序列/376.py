'''
@Author: 拎把木剑当大侠
@Description: 
@Date: 2019-04-18 18:32:22
@LastEditTime: 2019-04-18 18:45:58
'''


class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        m = 1
        n = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                m = n+1
            elif nums[i] < nums[i-1]:
                n = m+1
        return max(m, n)


s = Solution()
nums = [1, 7, 4, 9, 2, 5]
print(s.wiggleMaxLength(nums))
