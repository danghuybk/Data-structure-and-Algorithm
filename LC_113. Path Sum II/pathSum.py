class Solution:
    def pathSum(self, root: TreeNode, target_sum: int) -> List[List[int]]:
        output, stack = [], []
        if root:
            stack.append((root, root.val, [root.val]))
        while stack:
            cur_node, cur_sum, path = stack.pop()
            
            if not cur_node.left and not cur_node.right and cur_sum == target_sum:
                output.append(path[:])
            
            if cur_node.right:
                stack.append((cur_node.right, cur_sum + cur_node.right.val, path + [cur_node.right.val]))
                
            if cur_node.left:
                stack.append((cur_node.left, cur_sum + cur_node.left.val, path + [cur_node.left.val]))

        return output
