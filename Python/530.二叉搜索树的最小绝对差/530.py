'''
@Author: 拎把木剑当大侠
@Description: 
@Date: 2019-01-18 11:03:18
@LastEditTime: 2019-01-18 11:37:56
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        cur = pre = residual = None
        # 右子树->根节点->左子树
        # 得到从大到小的序列

        def trav(root):
            # nonlocal使用外层变量
            nonlocal cur, pre, residual
            if root.right:
                trav(root.right)
            if cur:
                cur, pre = root.val, cur
                residual = min(residual, pre-cur) if residual else pre-cur
            else:
                cur = root.val
            if root.left:
                trav(root.left)
        trav(root)
        return residual
