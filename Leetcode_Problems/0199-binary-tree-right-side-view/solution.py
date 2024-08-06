# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Approach:

# Initiate the list of the right side view rightside.

# Initiate two queues: one for the current level, and one for the next. Add root into nextLevel queue.

# While nextLevel queue is not empty:

# Initiate the current level: currLevel = nextLevel, and empty the next level nextLevel.

# While the current level queue is not empty:

# Pop out a node from the current level queue.

# Add first left and then right child node into nextLevel queue.

# Now currLevel is empty, and the node we have in hands is the last one, and makes a part of the right side view. Add it into rightside.

# Return rightside.
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        next_level = deque([root,])

        rightside = []

        while next_level:
            curr_level = next_level
            next_level = deque()

            while curr_level:
                node = curr_level.popleft()

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            rightside.append(node.val)

        return rightside
        
