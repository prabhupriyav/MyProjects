def get_middle(s):
    
    length = len(s)
    if length%2 != 0:
        print(s[length//2])
        return s[length//2]
    else:
        print(s[length//2-1]+s[length//2])
        return (s[length//2-1]+s[length//2])
    
def get_compare(s,m):
    if s == m:
        return True
    else:
        return False
    
get_compare(get_middle("test"),"es")
