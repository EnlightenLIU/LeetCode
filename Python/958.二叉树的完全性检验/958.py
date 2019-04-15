'''
@Author: 拎把木剑当大侠
@Description: 
@Date: 2019-04-15 21:08:16
@LastEditTime: 2019-04-15 21:08:27
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
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
            for nd in q:
                if flag:
                    if nd.left or nd.right:
                        return False
                if nd.left and nd.right:
                    qq.append(nd.left)
                    qq.append(nd.right)
                elif nd.left:
                    qq.append(nd.left)
                    flag = 1
                elif nd.right:
                    return False
                else:
                    flag = 1
            q = qq
        return True
