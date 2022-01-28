def narcissistic(value):
    sum1 = 0
    list1 = []
    val = str(value)
    for i in val:
        list1.append(i)
    print(list1)
    if len(list1) <= 1:
        return True
    else:
        for j in range(0,len(list1)):
            sum1 = sum1 + pow(int(list1[j]), len(list1))
        if sum1 == value:
            return True
        else:
            return False
narcissistic(153)
