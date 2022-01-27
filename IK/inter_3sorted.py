def find_intersection(arr1, arr2, arr3):
    # Write your code here
    i = 0
    j = 0
    k = 0
    array = []
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            array.append(arr1[i])
            i+=1
            j+=1
            k+=1
        elif arr1[i] <= arr2[j] and arr1[i] <= arr3[k]:
            i+=1
        elif arr2[j] <= arr1[i] and arr2[j] <= arr3[k]:
            j+=1
        else:
            k+=1
    if len(array) >=1:
        return array
    else:
        return [-1]
