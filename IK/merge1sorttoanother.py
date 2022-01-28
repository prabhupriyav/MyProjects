def merger_first_into_second(arr1, arr2):
   
    arr1len = len(arr1)
    arr2len = len(arr1)*2
    start = 0
    end = arr2len
    mid = start + (end-start) // 2
    i = start
    j = mid
    k=0
    temp = []
    while i <= mid-1 and j <= arr2len -1:
        arr2[j] = arr1[i]
        i+=1
        j+=1
    
    for k in range(len(arr2)):
       
        for l in range(k+1, len(arr2)-1):
            if arr2[k] < arr2[l]:
                temp.append(arr2[k])
            else:
