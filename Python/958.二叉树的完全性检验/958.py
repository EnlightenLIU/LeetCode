'''
@Author: 拎把木剑当大侠
@Description: 
@Date: 2019-04-15 21:08:16
@LastEditTime: 2019-04-15 21:32:15
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        q = [root]
        flag = 0
        while q:
            qq = []
            for node in q:
                if flag:
                    if node.left or node.right:
                        return False
                    if node.left and node.right:
                        return False
                if node.left and node.right:
                    qq.append(node.left)
                    qq.append(node.right)
                elif node.left:
                    qq.append(node.left)
                    flag = 1
                elif node.right:
                    return False
                else:
                    flag = 1
            q = qq
        return True
