'''
@Author: 拎把木剑当大侠
@Description: 
@Date: 2019-01-18 16:38:57
@LastEditTime: 2019-01-18 16:48:02
'''


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        self.auxPathSum(root, sum, [], res)
        return res

    def auxPathSum(self, root, sum, cur_list, cur_lists):
        if not root:
            return
        sum -= root.val
        if sum == 0 and not root.left and not root.right:
            cur_lists.append(cur_list + [root.val])
            return
        if root.left:
            self.auxPathSum(root.left, sum, cur_list + [root.val], cur_lists)
        if root.right:
            self.auxPathSum(root.right, sum, cur_list + [root.val], cur_lists)


'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root, ms, s, ans, cur):
        ms += root.val
        cur.append(root.val)
        if not root.left and not root.right and ms == s:
            ans.append(cur[:])
        if root.left:
            self.dfs(root.left, ms, s, ans, cur)
        if root.right:
            self.dfs(root.right, ms, s, ans, cur)
        cur.pop()
            
    
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = []
        if root:
            self.dfs(root, 0, s, ans, [])
        return ans
'''
