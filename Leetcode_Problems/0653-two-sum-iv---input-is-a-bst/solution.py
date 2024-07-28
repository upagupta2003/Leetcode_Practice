# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        lst = []
        self.inorder(root, lst)
        l, r = 0, len(lst) - 1
        while l < r:
            s = lst[l] + lst[r]
            if s == k:
                return True
            elif s < k:
                l += 1
            else:
                r -= 1
        return False

    def inorder(self, root: TreeNode, lst: List[int]) -> None:
        if not root:
            return
        self.inorder(root.left, lst)
        lst.append(root.val)
        self.inorder(root.right, lst)
