def find_combinations(n, k):
    
    result = []
    slate=[]
    def helper(n,i,k,slate):
        if len(slate) == k:
            result.append(slate[:])
            return
        if i == n+1:
            return
        helper(n,i+1,k,slate)
        slate.append(i)
        helper(n,i+1,k,slate)
        slate.pop()
    helper(n,1,k,slate)
    return result
