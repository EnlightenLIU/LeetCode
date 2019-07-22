class Solution:
    def subsetsWithDup(self, nums):
        if not nums: return []
        nums.sort()
        res = [[]]
        cur = []
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                cur = [tmp + [nums[i]] for tmp in cur]
            else:
                cur = [tmp + [nums[i]] for tmp in res]
            res += cur
        return res

s=Solution()
nums=[1,2,2]
result=s.subsetsWithDup(nums)
print(result)