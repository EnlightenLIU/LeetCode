'''
@Author: 拎把木剑当大侠
@Description: 
@Date: 2019-04-28 14:34:34
@LastEditTime: 2019-04-28 14:36:00
'''
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N == 1:
            return [TreeNode(0)]
        if N % 2 == 0:
            return []

        res = []

        left_num = 1
        right_num = N-2

        while(right_num > 0):
            lefts = self.allPossibleFBT(left_num)
            rights = self.allPossibleFBT(right_num)
            for i in range(len(lefts)):
                for j in range(len(rights)):
                    root = TreeNode(0)
                    root.left = lefts[i]
                    root.right = rights[j]
                    res.append(root)
            left_num += 2
            right_num -= 2
        return res
