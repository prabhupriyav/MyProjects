def solution(s):
    n = 2
    list1 = []
    for i in range(0,len(s),n):
        
        if len(s[i:i+n]) < 2:
            list1.append(s[i:i+n]+'_')
        else:
            list1.append(s[i:i+n])
    return list1
solution('12345fa')
