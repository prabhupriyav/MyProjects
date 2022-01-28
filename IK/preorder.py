def preorder(root):
    if root is None:
       return []
    result = []
    def dfs(node):
        if node.left_ptr is None and node.right_ptr is None:
             result.append(node.label)
             return
        result.append(node.label)
        if node.left_ptr is not None:
           dfs(node.left_ptr)
        if node.right_ptr is not None:
            dfs(node.right_ptr)
    dfs(root)
    return result
