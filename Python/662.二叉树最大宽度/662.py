# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        Max = 0
        #构造（TreeNode, index）的二元组来记录每个非空节点的位
        queue = [(root,0)]
        while queue:
            size = len(queue)
            LEN = queue[-1][1]-queue[0][1]+1
            Max = max(Max, LEN)
            for i in range(size):
                node = queue.pop(0)
                if node[0].left:
                    queue.append((node[0].left, 2*node[1]))
                if node[0].right:
                    queue.append((node[0].right, 2*node[1]+1))
        return Max