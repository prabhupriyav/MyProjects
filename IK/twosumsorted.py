def pair_sum_sorted_array(numbers, target):
    result = []
    k = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                k+=1
                result.append(i)
                result.append(j)
                return result
    if k == 0:
        return [-1,-1]
