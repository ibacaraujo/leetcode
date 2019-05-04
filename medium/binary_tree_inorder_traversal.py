# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.result = []
        
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root == None:
            return self.result
        self.inorderTraversal(root.left)
        #self.inorderTraversal(root.val)
        self.result.append(root.val)
        return self.inorderTraversal(root.right)
        
