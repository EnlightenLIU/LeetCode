# #超时
# class Solution:
#     def containsNearbyAlmostDuplicate(self, nums, k, t):
#         l=len(nums)
#         for i in range(l-1):
#             for j in range(i+1,l):
#                 if abs(i-j)<=k and abs(nums[i]-nums[j])<=t:
#                     return True
#         return False


# 如果： | nums[i] - nums[j] | <= t
# 式a
# 等价： | nums[i] / t - nums[j] / t | <= 1
# 式b
# 推出： | floor(nums[i] / t) - floor(nums[j] / t) | <= 1
# 式c
# ​等价： floor(nums[j] / t) ∈ {floor(nums[i] / t) - 1, floor(nums[i] / t), floor(nums[i] / t) + 1}
# 式d
#
# 其中式b是式c的充分非必要条件，因为逆否命题与原命题等价，所以：
# 如果： floor(nums[j] / t) ∉ {floor(nums[i] / t) - 1, floor(nums[i] / t), floor(nums[i] / t) + 1}
# 非d
# 推出： | nums[i] - nums[j] | > t
# 非a
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        import collections
        dic = collections.OrderedDict()
        if k<1 or t<0: return False
        for n in nums:
            key=n//t if t else n
            for m in [dic.get(key-1),dic.get(key),dic.get(key+1)]:
                if m!=None and abs(n-m)<=t:
                    return True
            if len(dic)==k:
                dic.popitem(last=False)
            dic[key]=n
        return False





s=Solution()
nums=[1,5,9,1,5,9]
k=2
t=3
print(s.containsNearbyAlmostDuplicate(nums,k,t))