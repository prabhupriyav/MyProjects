def allPathsOfABinaryTree(root):
    
    if root is None:
        return []
    result = []
    def helper(node,slate):
        slate.append(node.val)
        if node.left_ptr == None and node.right_ptr == None:
            result.append(slate[:])
        if node.left_ptr is not None:
            helper(node.left_ptr,slate)
        if node.right_ptr is not None:
            helper(node.right_ptr,slate)
        slate.pop()
    helper(root,[])
    return result
