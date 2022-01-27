def find_all_well_formed_brackets(n):

    res = []
    helper(n,0,0,[],res)
    return res
def helper(n,left,right,slate,res):
    if right>left or left > n or right > n:
        return
    if left == n and right == n:
        res.append(''.join(slate))
        return
    slate.append('(')
    helper(n,left+1,right,slate,res)
    slate.pop()
    slate.append(')')
    helper(n,left,right+1,slate,res)
    slate.pop()
