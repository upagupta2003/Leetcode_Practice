# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        '''
If the key is smaller than the root's value, it recursively calls deleteNode on the left subtree.
If the key is greater than the root's value, it recursively calls deleteNode on the right subtree.
If the key is found (root.val == key), it checks for the presence of child nodes. If there is no left child, it returns the right child, and vice versa. If both child nodes are present, it finds the minimum value in the right subtree (temp.left), assigns it  to the root's value, and recursively deletes that minimum node from the right subtree.
        '''
        if not root: return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left: return root.right
            if not root.right: return root.left

            if root.left and root.right:
                temp = root.right
                while temp.left: temp = temp.left
                root.val = temp.val
                root.right = self.deleteNode(root.right, root.val)
        
        return root  
