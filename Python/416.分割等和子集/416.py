class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''
        回溯思想: 先排序数组来减少回溯的节点, 然后通过递归, 遍历所有的可能
        '''
        s = sum(nums)
        # 假设可以拆分为两个和相等的子集, 数组的和是子集和的两倍, 一定是偶数
        if s % 2 == 1:
            return False
        n = len(nums)
        nums_sort = sorted(nums, reverse=True)

        # 假设可以找到和为整个数组和一半的子集, 那么剩下的就是另一个子集
        def findPartition(remain, index):
            print(index, remain)
            if remain == 0:
                return True
            if index < n and remain < nums_sort[index]:
                return False
            for i in range(index, n):
                print(index, remain, i, nums_sort[i])
                # !!! 回溯的节点, 不停的枚举试错, 一旦成功返回true
                if findPartition(remain - nums_sort[i], i + 1):
                    return True
            return False

        return findPartition(s // 2, 0)
s = Solution()
print(s.canPartition([1,1,2,3,5]))